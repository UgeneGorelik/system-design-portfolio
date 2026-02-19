Goal: Design a CDN (Content Delivery Network)

A CDN should:

Serve static assets (images, JS, video, files)

Reduce latency via geo-distribution

Scale to massive traffic

Be fault tolerant

Handle cache misses

Support encryption at rest

Apply rate limiting & logging

🏗 High-Level Architecture

Core components:

Client

API Gateway

Rate Limiting Service

Metadata Service

Storage Service

Secrets Management Service (for encryption keys)

Origin Service

Logging Service

🔁 Request Flow (Asset Present in CDN)

Client → API Gateway

API Gateway → Rate Limiting

API Gateway → Metadata Service

Metadata → returns storage host ID + path

API Gateway → Storage Service

(If encrypted)

API Gateway → Secrets Service → get key

Decrypt asset

Return asset to client

Log request

🔁 Request Flow (Cache Miss)

Client → API Gateway

Rate limit check

Metadata lookup → not found

API Gateway → Origin Service

Stream asset back to client

Encrypt asset (if required)

Store in Storage Service

Store key in Secrets Management

Update Metadata

Write-through caching model.

🗂 Storage Layer

Assets may:

Be split into blocks

Be replicated across storage hosts

Be stored encrypted

Metadata stores:

File → storage host mapping

Block mapping

Origin location

Encryption info

🔐 Encryption Design

Assets encrypted at rest

Keys stored separately (Secrets Service)

API Gateway is crypto boundary

For large files:

Fetch blocks

Decrypt per block

Stream to user

Security principle:

Data and keys are never stored together.

⚡ Scaling Strategy
Horizontal scaling

API Gateways behind load balancer

Storage nodes distributed

Metadata replicated

Stateless gateway layer

Geo-distribution

Edge nodes near users

DNS-based routing

Latency-based routing

🚦 Rate Limiting

Prevent abuse:

Token bucket / leaky bucket

Per user / IP quotas

Enforced before heavy operations

📊 Logging & Monitoring

Log:

Request latency

Cache hit/miss

Error rate

Traffic volume

Used for:

Capacity planning

Abuse detection

Performance tuning

🧠 Key Design Tradeoffs
1️⃣ Cache strategy

Write-through vs write-back

TTL expiration

LRU eviction

2️⃣ Consistency

Eventual consistency between metadata and storage

Handling stale cache

3️⃣ Availability vs consistency

CDN favors availability (AP in CAP).

📈 Bottlenecks

Metadata service (must scale)

Storage bandwidth

API Gateway CPU (especially if decrypting large files)

Mitigation:

Sharding

Replication

Block-level parallelism