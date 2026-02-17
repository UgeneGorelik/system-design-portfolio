🔹 Large-Scale System Design Concepts

These are the main strategies and building blocks for designing high-scale, reliable systems.

1️⃣ Throttling

Purpose: Prevent overload and protect critical services.

Limits the number of requests a client or service can make in a given time window.

Protects databases, caches, and downstream services from spikes.

Common strategies:

Token Bucket / Leaky Bucket – allow bursts but control sustained rate.

Fixed Window / Sliding Window – simple counters per time interval.

Example: Limiting users to 10 feed fetch requests per second.

Why it matters at scale: Without throttling, sudden spikes can take down your backend or cause cascading failures.

2️⃣ Queuing (Message Queues / Asynchronous Processing)

Purpose: Decouple services and handle bursts.

Incoming requests or jobs are placed into a queue.

Downstream workers poll or subscribe and process jobs at their own rate.

Benefits:

Smooths traffic spikes

Enables asynchronous processing

Improves reliability and failure isolation

Common tools: Kafka, RabbitMQ, SQS, Google Pub/Sub

Example:

Content ingestion → moderation → queue → feed processor

3️⃣ Caching

Purpose: Reduce latency and load on databases or APIs.

Store frequently-read data closer to the client or service.

Types:

In-memory cache: Redis, Memcached

CDN: CloudFront, Akamai

Caching strategies:

Write-through: Cache updated at the same time as DB

Write-back: DB updated asynchronously, cache is source of truth temporarily

Cache eviction policies: LRU (Least Recently Used), TTL (time-to-live)

Example:

Store latest news feed items in Redis for fast retrieval

Avoid hitting HDFS or DB for every request

4️⃣ Exponential Retry

Purpose: Improve reliability without overloading systems.

When a request fails (due to network, downstream service, etc.), retry with increasing delays.

Often combined with jitter to avoid thundering herd problems.

Pattern:

retry_delay = base_delay * 2 ^ attempt_number + random_jitter


Why it matters: Helps transient failures recover gracefully without cascading overloads.

5️⃣ Distributed Databases

Purpose: Store massive amounts of data reliably across multiple nodes and regions.

Concepts:

Sharding / Partitioning – split data across multiple nodes

Replication – maintain multiple copies for fault tolerance

Consistency models:

Strong consistency → all replicas immediately consistent

Eventual consistency → replicas converge over time

Examples: Cassandra, DynamoDB, CockroachDB, MongoDB (sharded)

Trade-offs: CAP theorem – you can’t have Consistency, Availability, and Partition tolerance all at the same time.

6️⃣ Other Core Scaling Patterns

Rate Limiting – protect services at the edge (API Gateway)

Load Balancing – distribute traffic across multiple service instances

Circuit Breakers – prevent retries from overwhelming a failing service

Bulkheads / Isolation – isolate failures to prevent system-wide crashes

Event Sourcing – record state changes as a sequence of events (good for auditing, high-scale writes)

CQRS (Command Query Responsibility Segregation) – separate read/write models for efficiency at scale

Partition-tolerant messaging – ensure messages aren’t lost during node failures