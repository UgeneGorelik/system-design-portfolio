Database Design
1️⃣ Users Table (Distributed SQL)

Stores user metadata and preferences.

Column	Type	Description
user_id	BIGINT (PK)	Unique user identifier
name	VARCHAR(100)	User display name
email	VARCHAR(255)	User email (optional)
selected_topics	ARRAY/VARCHAR	Up to 3 topics selected by user
last_active_at	TIMESTAMP	Last activity timestamp
created_at	TIMESTAMP	Account creation timestamp
updated_at	TIMESTAMP	Last update timestamp

Notes:

Sharded / partitioned by user_id for horizontal scaling.

Cached in Redis for fast access to preferences and metadata.

2️⃣ Posts Table (Distributed SQL)

Stores post metadata, links to HDFS and media.

Column	Type	Description
post_id	BIGINT (PK)	Unique post identifier
author_id	BIGINT (FK)	References Users.user_id
title	VARCHAR(150)	Post title
body	TEXT	Post body content (max 10,000 chars)
created_at	TIMESTAMP	Post creation time
topics	ARRAY/VARCHAR	1–3 topics/tags
media_urls	ARRAY/VARCHAR	URLs from Media Service / CDN
status	ENUM	'pending', 'approved', 'rejected'

Notes:

Status is updated after moderation.

Posts are precomputed in ETL and cached in Redis.

3️⃣ Media Table (Distributed SQL / Optional)

Tracks media uploaded for posts.

Column	Type	Description
media_id	BIGINT (PK)	Unique media identifier
post_id	BIGINT (FK)	Associated post
url	VARCHAR(500)	CDN URL for media
size	INT	Size in bytes
media_type	ENUM	'image', 'video', etc.
created_at	TIMESTAMP	Upload timestamp