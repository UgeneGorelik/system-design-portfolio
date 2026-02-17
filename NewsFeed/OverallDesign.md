News Feed System: Flow Explanation

This document explains the data flow and architecture of a scalable news feed system designed to handle text and media content, with precomputed feeds, caching, distributed metadata, and fast media delivery via CDN.

1️⃣ Overview

The system is designed to:

Deliver personalized news feeds with low latency

Support high-volume content ingestion and media uploads

Precompute feeds for fast retrieval

Use distributed caching and SQL metadata storage

Handle images and media efficiently via a Media Service and CDN

Key components include:

Backend1 (Feed API) – serves feeds and post data to users

Redis Cache – stores precomputed feeds and metadata

Distributed SQL (Zookeeper-managed) – stores user and post metadata

HDFS / Object Storage – stores raw posts and media files

ETL / Feed Preparation – precomputes feeds for fast delivery

Media Service & CDN – handles media uploads and delivery

News Ingestion & Moderation – handles post submissions and approval

Message Queue & Backend2 – processes asynchronous updates

2️⃣ Write / Ingestion Flow

Content Submission:

Clients submit posts via News Ingestion Service.

Posts may include media files (images, videos).

Moderation:

Moderation Service filters inappropriate text or media.

Posts are marked as approved, rejected, or pending.

Media Handling:

Media files are uploaded to Media Service.

Media Service stores files in object storage or HDFS and provides CDN URLs.

Queueing & Async Processing:

Approved posts are pushed to a Message Queue.

Backend2 (Async Processor) polls the queue to:

Write posts to HDFS

Update Metadata in distributed SQL

Trigger ETL feed precomputation

3️⃣ Feed Preparation / ETL

ETL Job precomputes feeds in advance for each user.

Steps include:

Filtering posts by user-selected topics

Sorting posts in reverse chronological order

Resolving media URLs via Media Service / CDN

Storing the computed feed in Redis Cache

Precomputed feeds reduce on-demand database queries and improve latency.

4️⃣ Read / Feed Delivery Flow

User Request:

User sends a request via API Gateway.

API Gateway routes to Backend1 (Feed API).

Cache Lookup:

Backend1 checks Redis Cache for a precomputed feed.

Cache uses consistent hashing to distribute data evenly across nodes.

Fallback / ETL:

If the feed is not in cache, Backend1 requests ETL service to compute it on-demand.

ETL retrieves raw posts from HDFS and metadata from Distributed SQL.

Media Delivery:

For posts with media, Backend1 includes CDN URLs.

Users fetch images and videos directly from CDN, reducing load on backend.