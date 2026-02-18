Load Balancing – Overview

Load balancing is the practice of distributing incoming network or application traffic across multiple servers to ensure:

High availability

Fault tolerance

Optimal resource utilization

Low latency for users

1️⃣ Why Load Balancing is Needed

Single server can become a bottleneck under heavy traffic

Prevent downtime if a server fails

Scale horizontally by adding more servers

Support geographical distribution for low-latency access

2️⃣ Types of Load Balancers
Type	Description	Example
Hardware Load Balancer	Dedicated appliance for high-throughput environments	F5 BIG-IP, Citrix ADC
Software Load Balancer	Software-based, flexible, runs on commodity servers	Nginx, HAProxy, Envoy
Cloud Load Balancer	Managed service by cloud provider	AWS ELB, GCP Cloud LB, Azure LB
3️⃣ Load Balancing Algorithms
Algorithm	How It Works	Pros	Cons
Round Robin	Distribute requests evenly in order	Simple, fair	Ignores server load
Least Connections	Send request to server with fewest active connections	Better for uneven workloads	Needs tracking connections
IP Hash	Hash client IP → consistent server assignment	Sticky sessions without cookies	Can unevenly distribute load
Weighted Round Robin / Least Connections	Assign weights based on server capacity	Handles heterogeneous servers	Slightly more complex
4️⃣ Types of Load Balancing
A. Layer 4 (Transport Layer)

Works at TCP/UDP level

Routes traffic based on IP address and port

Fast, less overhead, cannot inspect HTTP headers

B. Layer 7 (Application Layer)

Works at HTTP/HTTPS level

Can route based on URL, cookies, headers, content

Supports sticky sessions, A/B testing, and blue/green deployments

5️⃣ Load Balancing in System Design

Web applications: balance traffic across multiple app servers

CDN + LB: CDN handles edge caching + LB distributes requests to origin servers

Microservices: internal service discovery often includes load balancing

Database read replicas: LB for read queries to multiple replicas

6️⃣ Load Balancer Architecture Flow
Client
   |
   v
+-----------------+
| Load Balancer   | --> routes to Server 1
| (Round Robin)   | --> routes to Server 2
+-----------------+
        |
        v
   Application Servers


Can be global (across regions) or local (within a region)

Often combined with health checks → automatically avoids unhealthy servers