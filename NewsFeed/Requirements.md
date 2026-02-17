📌 News Feed – Requirements Summary
1️⃣ Functional Requirements
User Preferences

Users can select up to 3 tags (from a maximum of 100 tags).

Tags represent topics of interest.

News Feed Retrieval

Fetch news items in reverse chronological order (approximate is acceptable).

Pagination: 10 items per request, up to 1,000 items per user session.

Only English-language items initially.

Same feed regardless of geographic location (no personalization at first).

News Item Structure

Each item contains:

Text field (≤10,000 characters)

UNIX timestamp (creation time)

1–3 associated tags

(Optional future scope: 0–10 images, ≤1MB each)