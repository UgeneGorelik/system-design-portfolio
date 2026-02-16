📌 Project Overview

This system is a classified ads web application, similar to Craigslist, designed for high scale and availability.
It must support billions of users and local posting/search while maintaining high performance, scalability, and security.

🧩 Functional Requirements

User Roles

Viewer: Can browse/search posts, apply filters, report fraud.

Poster: Can create posts, renew posts weekly, and optionally set posts to auto-delete after one week.

Post Management

Create, update, and delete posts.

Renew posts automatically or manually each week.

Posts auto-expire after a week (optional).

Search & Discovery

Filter posts by category, location, or other metadata.

Search must prioritize local posts.

Reporting & Moderation

Report posts for fraud or inappropriate content.

System should flag suspicious activity for review.

⚡ Non-Functional Requirements

Scalability

Handle billions of users and hundreds of millions of posts.

Support heavy read traffic (browsing/search) and moderate write traffic (posting/renewals).

Performance

Page load & redirect times <100ms ideally.

Search queries return in <200ms for local results.

Availability

System must be highly available (target SLA ≥ 99.99%).

Redundancy in all critical components.

Security

Prevent fraudulent posts and spam.

Data privacy for user information.

Data Storage

Not too storage intensive; posts can expire to reclaim space.

Posts auto-deleted after one week to minimize storage usage.

🗂 Core Entities
Entity	Description
Viewer	User who browses/searches posts and reports fraud.
Poster	User who creates posts and manages weekly renewal.
Post	Content submitted by Poster, with optional auto-expiration.
📝 Notes / Design Constraints

Locality matters: search and browsing should prioritize posts in the user’s area.

System must support weekly renewals without creating duplicate posts unnecessarily.

Should scale gracefully for billions of users while remaining lightweight in storage.

High availability, performance, and security are mandatory.

If you want, the next step is to create the 02-entities.md file for this project, turning these users and posts into domain objects with relationships, attributes, and constraints.