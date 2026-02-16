Redis_Cache

To handle high read traffic on popular posts and meet latency targets (e.g., 1-second P99), use caching. 
Implement an LRU cache in Redis with the post ID as the key and the HTML page as the value. 
An image service can cache images separately. 
Since posts are mostly static, cache staleness is minimal, but if a post is updated, the cache should be refreshed.

Cdn
urpose: Offload traffic from your origin servers, reduce latency, and improve P99 response times for high-read posts.

How it works: The CDN caches static content (HTML pages, images, assets) 
at edge servers close to users. Popular posts get served from the nearest edge, not the main server.

CDN caches the same posts (and images) globally, reducing repeated hits to your servers.

Cache invalidation: When a post is updated, both the Redis cache and the CDN edge caches need to be refreshed.