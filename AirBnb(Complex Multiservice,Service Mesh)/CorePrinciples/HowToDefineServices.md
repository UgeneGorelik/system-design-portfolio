Step 1: Start from business functionality

Every service should correspond to a coherent domain or business capability.

Process:

List all user-facing features and back-office processes.

Guests: search, book, cancel, review.

Hosts: create listing, update availability, manage bookings.

Admins: approve listings, enforce regulations.

Group related features into domains.

Booking & availability → Booking domain.

Listing creation → Listing domain.

Recommendations → Personalization domain.

This ensures services have a clear single responsibility, making them easier to scale, deploy, and maintain.

Step 2: Consider non-functional requirements (NFRs)

Some services may share functional domains but have very different requirements for availability, latency, and consistency. Those differences often justify separate services.

Example from Airbnb:

Service	NFRs
Booking Service	High availability, low latency, strong performance
Availability Service	High read scalability; writes less frequent, consistency important during booking
Recommender Service	Lower criticality, eventual consistency OK

If two components have drastically different scaling needs or failure impact, separate them into different services.

Step 3: Identify cross-cutting services

Some functions are used by multiple domains — these are good candidates for shared services:

Availability Service → used by both Booking and Listing

Regulations Service → used by Booking and Listing to ensure compliance

Analytics / Logging / Metadata Services → used across all services internally

Shared services reduce duplication and centralize expertise, but should remain decoupled from critical revenue flows to avoid bottlenecks.

Step 4: Map each service to team ownership

If your organization has multiple teams, it’s often better to give each team one service or domain.

Booking Team → Booking Service

Host Management Team → Listing Service

Compliance Team → Regulations Service

AI / Data Team → Recommender Service

Clear ownership improves maintainability and reduces cross-team dependencies.

Step 5: Check dependencies and data boundaries

A service should own its data and not rely heavily on other services for its internal operations.

If multiple services need the same data, consider separating the data store and creating a shared service (e.g., Availability Service) instead of sharing a database.

Step 6: Iterate and validate

Start with a high-level list of candidate services.

For each, ask:

Does it represent a distinct business capability?

Does it have different NFRs from other services?

Can it be developed, deployed, and scaled independently?

Refine the boundaries over time as the system grows.

Airbnb Example Revisited (Expanded)
Service	Responsibility	Notes / NFRs / Ownership
Booking Service	Handles guest bookings	Critical revenue service; high availability, low latency; owned by Booking Team
Listing Service	Hosts create/manage listings	Different scaling & availability than Booking; owned by Host Management Team
Availability Service	Tracks room availability	Used by Booking & Listing; must scale reads; strong consistency during booking; shared service
Approval Service	Manages operations approval	For certain listing changes; moderate latency acceptable
Recommender Service	Personalized recommendations	Eventual consistency OK; internal ads-like system; owned by AI/Data Team
Regulations Service	Compliance & local regulations	Helps Booking/Listing comply; owned by Compliance Team
Payment Service	Process payments	Strong consistency, PCI compliance; critical revenue impact
Analytics / Logging / Metadata Services	Internal metrics, logs, metadata	Mostly internal; low criticality; used for monitoring & insights
Notification Service	Sends emails/SMS to guests & hosts	Can fail without breaking core booking flow; retry via queue

Notice how each service has a reason to exist: domain responsibility, scaling/NFR difference, or team ownership.