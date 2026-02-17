Components of Craigslist-Like System 
1️⃣ Clients / Frontend

Web browsers, mobile apps

Sends HTTP requests to backend

Displays posts, images, search results, user forms

2️⃣ GeoDNS / Regional Routing

Routes users to the nearest regional server/data center

Ensures low latency, high availability, and local post prioritization

Works with regional caches and DB replicas

3️⃣ Backend / API Servers

Stateless application servers

Handles all business logic synchronously:

Post creation, update, deletion

User signup/login

Post auto-expiration (via scheduled jobs or cron tasks)

Reporting / moderation

Horizontal scaling possible per region

4️⃣ SQL Database

Stores structured data:

Users

Posts metadata (denormalized)

Reports

Supports replication / sharding for scale

Post auto-deletion handled by backend jobs

5️⃣ Cache Layer

Optional in-memory cache (Redis / Memcached)

Stores hot posts per region

Reduces database load and improves read performance

6️⃣ Object Store (Images)

Stores images for posts (S3, Azure Blob, or self-hosted)

Backend stores image_address in DB

Served via CDN for fast delivery

Image processing (thumbnails, resizing) handled by backend

7️⃣ Monitoring & Observability

Logs, metrics, and alerts

Tracks latency, errors, post expiration, and region health