Goal: Design an Autocomplete System

Requirements:

Return top suggestions as user types

Low latency (<100ms)

High QPS (every keystroke triggers request)

Ranked by popularity / relevance

Real-time or near-real-time updates

Highly available

Examples:

Search bars

Product suggestions

Query suggestions (like Google)

E-commerce search (like Amazon)

🏗 High-Level Architecture

Core components:

Client (browser/mobile)

Load Balancer

API Gateway

Autocomplete Service

Cache Layer (Redis)

Search Data Store (Trie / index store)

Analytics / Logging Service

Offline Aggregation Pipeline

🔁 Request Flow (Normal Operation)

User types "iph"

Client → API Gateway

API Gateway → Cache (Redis)

If cache hit → return suggestions

If cache miss:

Query Autocomplete Service

Query data store (Trie / search index)

Rank suggestions

Store in cache

Return results

Log query

📦 Data Storage Design

Core challenge: Fast prefix lookup.

Common structures:

1️⃣ Trie (Prefix Tree)

O(k) lookup (k = prefix length)

Each node stores:

children

top N suggestions

Data Update Flow

Autocomplete data must update.

Offline Pipeline

Collect search logs

Aggregate frequency

Compute top suggestions

Rebuild Trie

Deploy new snapshot

Often batch updated every few minutes or hours.

Streaming updates possible but complex.

🧠 Scalability
Horizontal Scaling

Stateless API servers

Shared Redis cluster

Sharded prefix ranges (a–m, n–z)

Partitioning Strategy

Shard by:

First character

Hash(prefix)

Region

🚦 Rate Limiting

Because every keystroke triggers request:

Debounce on client (300ms)

Rate limit per IP

Protect against bots

🔥 Bottlenecks

Memory (Trie can be huge)

Cache hot keys

Cold start after deployment

Ranking recalculation cost

🧩 Key Design Tradeoffs
1️⃣ Precompute vs Compute On Demand

Precompute:

Faster

More memory

On demand:

Less memory

Higher latency

2️⃣ Real-time vs Batch Updates

Real-time:

Complex

Event streaming required

Batch:

Simpler

Slightly stale results