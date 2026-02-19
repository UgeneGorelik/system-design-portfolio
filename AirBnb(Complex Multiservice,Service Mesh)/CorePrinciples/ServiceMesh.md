What is a Service Mesh?

A service mesh is a dedicated infrastructure layer that manages service-to-service communication in a microservices architecture. Instead of each service having to handle networking, retries, load balancing, security, and observability, the service mesh does it automatically, often via a sidecar proxy injected next to each service.

Think of it like an air traffic control system for microservices:

Routing: It decides how requests flow between services.

Load balancing: It spreads requests across multiple instances of a service.

Retries and timeouts: It handles failures automatically.

Security: It can encrypt communication between services (mTLS).

Observability: It collects metrics, logs, and traces without modifying service code.

Key point: The service mesh doesn’t replace your services; it sits alongside them and makes their interactions more reliable and secure.

In your Airbnb example, instead of the Booking Service calling the Availability Service directly and implementing its own retry or timeout logic, the service mesh handles it. That way, you can scale, monitor, and secure service calls consistently across all services.


Service mesh is not “code you write” like a Python library

A service mesh (like Istio, Linkerd, Consul Connect) is infrastructure.

It runs outside your Python code, usually as sidecar proxies next to each microservice.

It intercepts network traffic between services and provides features like routing, retries, encryption, and observability.