from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import boto3
import redis
import uuid
from datetime import datetime
import os
import json
import time

# Environment variables
POSTS_TABLE = os.environ['POSTS_TABLE']
CACHE_ENDPOINT = os.environ.get('CACHE_ENDPOINT')
EVENT_STREAM = os.environ['EVENT_STREAM']
IMAGES_BUCKET = os.environ['IMAGES_BUCKET']

# AWS clients
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(POSTS_TABLE)
s3 = boto3.client('s3')
kinesis = boto3.client('kinesis')

# Redis cache
cache = redis.Redis.from_url(f"redis://{CACHE_ENDPOINT}:6379") if CACHE_ENDPOINT else None

# Throttling: simple in-memory
REQUESTS = {}
RATE_LIMIT = 5  # max requests per 10 seconds per IP
TIME_WINDOW = 10

app = FastAPI(title="Craigslist-style Backend")

class Post(BaseModel):
    title: str
    description: str
    poster_id: str
    location: str
    image_name: str = None  # Optional S3 image reference

# Simple throttling dependency
def throttle(ip: str):
    now = time.time()
    times = REQUESTS.get(ip, [])
    times = [t for t in times if now - t < TIME_WINDOW]
    if len(times) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    times.append(now)
    REQUESTS[ip] = times

@app.post("/post")
async def create_post(post: Post, request: Request):
    throttle(request.client.host)
    post_id = str(uuid.uuid4())
    item = post.dict()
    item.update({"id": post_id, "created_at": datetime.utcnow().isoformat()})

    # Save to DynamoDB
    table.put_item(Item=item)

    # Cache in Redis
    if cache:
        cache.set(f"post:{post_id}", json.dumps(item), ex=3600)

    # Send event to Kinesis
    kinesis.put_record(
        StreamName=EVENT_STREAM,
        Data=json.dumps(item),
        PartitionKey=post_id
    )

    # Optional: reference image in S3
    if post.image_name:
        s3.put_object(Bucket=IMAGES_BUCKET, Key=f"{post_id}/{post.image_name}", Body=b"")  # placeholder

    return {"post_id": post_id, "image_ref": f"s3://{IMAGES_BUCKET}/{post_id}/{post.image_name}" if post.image_name else None}

@app.get("/post")
async def get_post(id: str, request: Request):
    throttle(request.client.host)

    # Try Redis cache first
    if cache:
        cached = cache.get(f"post:{id}")
        if cached:
            return json.loads(cached)

    # Fallback to DynamoDB
    resp = table.get_item(Key={"id": id})
    item = resp.get("Item")
    if not item:
        raise HTTPException(status_code=404, detail="Post not found")

    # Update cache
    if cache:
        cache.set(f"post:{id}", json.dumps(item), ex=3600)

    return item
