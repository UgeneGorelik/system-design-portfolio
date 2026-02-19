Design Amazon Dashboard Top 10 (Top 10 best-selling / trending products)

Think of the homepage section like on Amazon showing:

“Top 10 in Electronics”

“Trending Now”

“Best Sellers”

This is essentially a real-time top-K aggregation system at massive scale.

🎯 Goal

Design a system that:

Shows Top 10 products

Updated near real-time

Per category

Per region

Possibly personalized

Extremely high read traffic

Very high write/update rate (orders)

🏗 High-Level Architecture

Core components:

Client

Load Balancer

API Gateway

Dashboard Service

Cache Layer (Redis)

Ranking Service

Event Stream (orders)

Aggregation / Stream Processing Layer

Persistent Store (NoSQL)

🔁 Read Path (User Loads Dashboard)

Client → API Gateway

API Gateway → Cache

If cache hit → return Top 10 list

If cache miss:

Query Ranking Store

Return result

Cache result (short TTL)

Reads must be extremely fast (<50ms).

🔁 Write Path (Order Happens)

User buys item

Order Service emits event

Event pushed to stream (e.g., Apache Kafka)

Stream processor updates counters

Recompute Top 10 per category

Update ranking store

Invalidate cache

🧠 Core Problem

Efficiently maintain Top K (K=10) over massive stream.

If naïve:

Re-sorting entire dataset = impossible

Instead use:

1️⃣ Min Heap (size K)

Per category:

Maintain heap of top 10

If new product count > min → replace

Time complexity:
O(log K) per update → very cheap


Real-Time vs Batch
Option 1: Real-Time Stream Processing

Use:

Kafka

Stream processor (e.g., Apache Flink)

Pros:

Fresh data

Dynamic trending

Cons:

More infra complexity