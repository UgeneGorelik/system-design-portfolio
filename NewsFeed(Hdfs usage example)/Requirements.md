News Feed System Design – Summary
Problem Statement

Design a social media-style news feed that shows users relevant posts from friends, pages, or followed accounts.

Goals:

Show most relevant content first (ranking)

Handle millions of users and billions of posts

Low-latency feed delivery (<100ms to render feed)

Scalable read/write paths

Requirements
Functional

Users can post content (text, images, videos)

Users can follow friends, pages, or hashtags

Users can like, comment, and share posts

News feed shows personalized ranked posts

Optional: real-time updates or push notifications

Non-Functional

High throughput (billions of posts/day)

Low read latency

High availability

Scalable storage for media and metadata

High-Level Architecture

Two main flows:

Write / Ingestion Path

Users create posts → Post Service → Primary DB / Object Storage (for media)

Event generated → Fan-out or feed aggregation pipeline

Read / Query Path

User requests feed → Feed Service → Query precomputed feed or pull from multiple sources

Ranking algorithm determines relevance

Feed cached for faster retrieval

Data Model

Posts Table

Column	Type	Notes
post_id	UUID / PK	Unique identifier
user_id	FK	Author
content	Text	Post text
media_url	String	Optional images/videos
created_at	Timestamp	Post timestamp
likes_count	Int	Aggregate count
comments_count	Int	Aggregate count

Follow Table
| follower_id | followee_id | timestamp |

Feed Table (optional precomputed)
| user_id | post_id | ranking_score | timestamp |

Feed Generation Models
1️⃣ Pull Model (On-demand)

When user opens feed, query posts of friends/followed accounts

Rank dynamically using scoring function (time decay, likes, relevance)

Pros: always fresh, simple

Cons: high latency for many friends/followed accounts

2️⃣ Push Model (Fan-out on write)

When a user posts, push it into all followers’ feeds

Store feed per user (denormalized)

Pros: low read latency

Cons: high write amplification (popular users with millions of followers)

Hybrid Model

Fan-out for “small” users (<1000 followers)

Pull for “mega influencers”

Ranking / Personalization

Combine signals:

Recency (new posts first)

Engagement (likes, shares, comments)

Relevance (content type, user interests)

Machine learning models for personalized ranking

Scaling Considerations

High Read vs Write Ratio: reads >> writes

Sharding / Partitioning:

Shard feeds by user_id

Shard posts by post_id or author_id

Caching Layer: Redis / Memcached for hot feeds

Object Storage + CDN: for media (images/videos)

Event-driven Architecture: Kafka / Kinesis for fan-out & aggregation

Optional Enhancements

Trending posts / hashtags

Real-time notifications

Feed deduplication

Spam / abuse detection

Data Flow (Conceptual)
User
  |
  |---> API / Load Balancer
           |
           v
       Post Service
           |
           +--> Primary DB (posts)
           +--> Object Storage (media)
           +--> Event Stream (Kafka)
                       |
                       v
              Feed Generation Service
                 /           \
       Push to followers     Pull-on-demand
           |                     |
           v                     v
         Feed Cache           Query posts + ranking
           |                     |
           v                     v
         User sees feed       User sees feed