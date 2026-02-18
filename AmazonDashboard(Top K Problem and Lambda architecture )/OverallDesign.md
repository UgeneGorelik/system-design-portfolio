Problem Statement

Design a system that returns the top 10 products by sales volume in real time or near real time.

Input: sales events (user purchases with product IDs, quantity, timestamp)

Output: list of top 10 products per category, region, or global

Scale: billions of events per day, millions of products

Core Concepts

Stream of events

Each sale generates a record: (user_id, product_id, quantity, timestamp)

System must ingest high-volume events continuously

Aggregation

Compute total sales per product

Maintain cumulative counts or running totals

Top-K selection

Keep only the top 10 products (per category/region/global)

Use efficient data structures for updates:

Min-Heap (size K): O(log K) insert/update

Optional approximate algorithms (Count-Min Sketch) for huge catalogs

Serving queries

Return top 10 products instantly for dashboards or APIs

Precompute results in memory or cache for low-latency reads

Scaling Patterns

CQRS (Command/Query Separation)

Commands: ingest sales events

Queries: serve top-K products

Event-driven / Streaming Architecture

Kafka / Kinesis for high-throughput event ingestion

Stream processors (Flink / Spark Streaming) maintain rolling counts

Batch Rollups

Hourly / daily / weekly aggregation reduces storage

Only top-K per window retained

Caching Layer

Redis / Memcached to store top-K per category/region for instant retrieval