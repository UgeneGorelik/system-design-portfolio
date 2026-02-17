API Contracts (Detailed)
1. Get User Feed
GET /feed
Parameters:
  - user_id (required) : ID of the user
  - limit (optional) : number of posts to return (default 10)
  - offset (optional) : pagination offset (default 0)
Response:
  - feed_items: array of posts
      - post_id
      - title
      - body
      - media_urls (array)
      - created_at (timestamp)
      - topics (array)
  - next_offset : for pagination
Notes:
  - Returns the user’s precomputed feed from cache if available
  - Supports reverse chronological ordering

2. Get Single Post
GET /post/{post_id}
Parameters:
  - post_id (required) : ID of the post
Response:
  - post_id
  - title
  - body
  - media_urls (array)
  - created_at (timestamp)
  - topics (array)
  - author_id
Notes:
  - Returns full post metadata and media URLs

3. Submit New Post
POST /post
Request Body:
  - author_id (required)
  - title (required, max 150 chars)
  - body (required, max 10,000 chars)
  - topics (optional, array, 1-3)
  - media_files (optional, array of URLs or file uploads)
Response:
  - post_id : newly created post ID
  - status : success/failure
Notes:
  - Media files should be uploaded via Media Service
  - Post goes through Moderation Service before being added to feed

4. List Topics
GET /topics
Response:
  - topics: array of available news topics/tags
Notes:
  - Users can select up to 3 topics of interest

5. Update User Preferences
POST /user/{user_id}/preferences
Request Body:
  - selected_topics (array, max 3)
Response:
  - status : success/failure
Notes:
  - Updates user’s selected topics for feed personalization

6. Get User Metadata
GET /user/{user_id}
Response:
  - user_id
  - selected_topics
  - last_active_at
Notes:
  - Useful for feed generation and analytics

7. Search Posts (Optional / Future)
GET /search
Parameters:
  - query (required) : keyword search
  - topics (optional) : filter by topic array
  - limit (optional)
Response:
  - feed_items : array of posts matching query
Notes:
  - Initially optional; can be added after core feed system is stable