How we decide what should be a service:

Step 1: Look at Bounded Contexts / Domains

A “service” usually corresponds to a bounded context in your business domain — a piece of functionality that:

Has its own distinct data

Can operate independently

Has clear responsibilities

May scale or fail independently

For Airbnb for example , you can group features into domains:

Domain	Responsibilities	Could be a Service?
User Management	Signup, login, profile, verification	✅ User Service
Listings	Create/edit listings, images, amenities	✅ Listings Service
Search	Filtering, location search, sorting	✅ Search Service
Booking & Availability	Reservations, calendar, conflict detection	✅ Booking Service
Payments	Payment processing, refunds	✅ Payments Service
Messaging	Guest ↔ Host communication	✅ Messaging Service
Reviews & Ratings	Post-booking reviews, aggregated ratings	✅ Reviews Service
Admin / Moderation	Fraud detection, reports	✅ Admin Service

Rule of thumb: if a domain can be logically separated and has its own data, it can be a service.

Step 2: Consider Scaling Needs

Even if something is small, you might want it as a separate service if:

It has very different scaling requirements

Example: Search and listing images might get millions of reads; you might scale them separately.

It requires different infrastructure

Example: Payment service must be PCI-compliant → separate service.

It has independent failure tolerance

Booking failing shouldn’t take down messaging or search.

Step 3: Think About Data Ownership

Each service should own its data.

Avoid multiple services directly writing to the same database (to prevent coupling).

Services communicate via API calls or async events (Kafka / Kinesis).

Example:

Booking Service owns bookings and availability tables.

Listing Service owns listings table and image references.

Search Service indexes listings for fast querying, but does not own the master listing data.

Step 4: Look at Integration / External Dependencies

Anything that interacts heavily with external systems may be a service:

Payments → Payment gateways

Notifications → Email, SMS, push notifications

Search indexing → Elasticsearch/OpenSearch

This allows you to replace or scale external dependencies without affecting the core backend.

Step 5: Ask Yourself These Questions for Each Feature

Does it have its own data and business rules?

Does it need different scaling than other parts of the system?

Does it need different security/compliance?

Can it fail without breaking other domains?

Does it make sense to deploy independently?

If the answer is mostly “yes,” it’s probably worth being a separate service.

TL;DR — How to Decide

Group by business domain → candidate service

Check data ownership → must own its DB

Check scaling/failure/security needs → justify separation

Use async communication where needed to decouple services