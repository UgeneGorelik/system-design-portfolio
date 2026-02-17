📌 Purpose

Defines the external contract of the system: endpoints, methods, request/response expectations, and basic constraints.
API design is interface-first to separate client integration from backend implementation.

🗂 Post Management Endpoints
HTTP Method	Endpoint	Description
GET	/post/{id}	Retrieve a specific post by ID.
DELETE	/post/{id}	Delete a specific post by ID (used for moderation or cleanup).
GET	/post	Retrieve all posts. Supports optional query parameters: search for text search, plus pagination filters like page and limit.
POST	/post	Create a new post.
PUT	/post	Update an existing post.
DELETE	/old_posts	Bulk deletion of expired or old posts (e.g., posts older than 1 week).
🗂 User Interaction Endpoints
HTTP Method	Endpoint	Description
POST	/contact	Send a message to a poster (contact functionality).
POST	/report	Report a post for fraud or inappropriate content.
🗂 User Management Endpoints

Accounts are minimal; only basic signup/login flows are required.

HTTP Method	Endpoint	Description
POST	/signup	Create a new user account.
POST	/login	Authenticate a user and return a session or token.
DELETE	/user/{id}	Delete a user account (admin or self-service).
🔍 Query Parameters & Notes

search={search_string} → full-text search across post content.

page and limit → optional pagination for listing endpoints (GET /post).

Optional filters can include:

category

location

date_posted

All read endpoints (GET) should favor local posts first based on user’s region.

DELETE /old_posts can be automated as a scheduled cleanup task.