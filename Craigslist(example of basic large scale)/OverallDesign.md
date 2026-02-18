Craigslist-Style System Design – Summary
Problem Statement

Design a large-scale online classifieds platform (like Craigslist) that allows users to:

Post listings (items, jobs, services, housing, etc.)

Search listings by keywords, category, location, and filters

Browse and view listings

Optionally message sellers

Scale: millions of listings, high read/write throughput

Requirements
Functional

User registration and authentication

CRUD for listings

Search and browse by category/location/filters

Optional messaging between users

Display top listings / trending posts

Non-Functional

High availability

Low-latency search (<100ms)

Horizontal scalability

Durable storage for millions of listings

Handling high read traffic

High-Level Architecture

Two main flows:

Write / Ingestion Path

Users create, update, or delete listings

Listings stored in primary database (SQL or NoSQL)

Images uploaded to object storage (S3 / blob storage)

Read / Query Path

Users browse or search listings

Search queries served via search engine (Elasticsearch / Solr)

Optional caching for popular searches

Data Model
Listing Table
Column	Type	Notes
listing_id	UUID / PK	Unique identifier
user_id	FK	Owner of listing
category	String	e.g., Jobs, Housing
title	String	Listing title
description	Text	Full description
location	Geo-coordinates	City / Zip for search
price	Decimal	Optional
created_at	Timestamp	Post creation
updated_at	Timestamp	Last update
status	Enum	Active / Expired / Deleted
Optional Supporting Tables

Users: user_id, name, email, etc.

Messages: sender_id, receiver_id, listing_id, message text, timestamp

Images: listing_id, image_url, metadata

Search Architecture

Elasticsearch / Solr: index listings for keyword + filter search

Inverted index: fast retrieval by keywords

Geospatial queries: support location-based search

Ranking / Sorting: by date, popularity, or relevance

Flow – Full CRUD + Search

Create Listing

User → API → Load balancer → Listing Service

Listing stored in Primary DB

Event triggered → Update Search Index

Update / Delete Listing

Similar flow; index updated or removed

Search / Browse

User query → Load balancer → Search Service

Search Service queries search index → returns matching listings

Optional caching for hot queries

View Listing

Listing details fetched from DB

Images served from object storage (CDN for low latency)

Messaging

Optional: messaging service queues messages to recipient

Stored in DB for history

Scaling Considerations

High Read vs Write Ratio

Reads >> Writes

Use Elasticsearch / Solr to offload reads from primary DB

Database Choices

Relational DB: consistent schema, strong relationships

NoSQL / Document DB: fast writes, flexible schema for listings

Caching

Redis or Memcached for popular listings and searches

Object Storage

Images / attachments in S3 / Blob storage + CDN

Partitioning / Sharding

By category, region, or listing_id for horizontal scalability

Eventual Consistency

Search index may lag slightly behind DB updates

Acceptable for most listings