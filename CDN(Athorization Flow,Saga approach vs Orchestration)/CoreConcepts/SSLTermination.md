SSL Termination – Overview

SSL/TLS termination is the point in a network where encrypted HTTPS traffic is decrypted so that internal systems can handle it in plain HTTP (or forward it encrypted to internal services).

1️⃣ Why SSL Termination is Used

Offload encryption work from backend servers → reduces CPU overhead

Centralized certificate management → easier to rotate/renew SSL certs

Simplify internal architecture → internal services can talk HTTP instead of HTTPS

Enable layer 7 routing / load balancing → inspect HTTP headers, path-based routing

2️⃣ How SSL Termination Works

Basic Flow:

Client (HTTPS) --> Load Balancer / Reverse Proxy (SSL Termination)
                      |
                 Decrypted HTTP
                      |
                Internal Servers


Client connects over HTTPS

Load Balancer / Proxy terminates SSL/TLS handshake

Traffic inside the network can be unencrypted HTTP

Optional: re-encrypt traffic to backend (SSL passthrough) for end-to-end security

3️⃣ Common Locations for SSL Termination
Layer	Example	Notes
Load Balancer / CDN	AWS ELB, CloudFront, Akamai	Offloads SSL from backend servers
Reverse Proxy	Nginx, HAProxy	Terminates SSL and routes traffic internally
Application Server	Optional, only if LB doesn’t terminate	Rare, increases CPU load
4️⃣ SSL Termination vs SSL Passthrough
Feature	SSL Termination	SSL Passthrough
Where decryption happens	LB / Proxy	Backend server
CPU load on backend	Low	High
Inspect HTTP headers	Yes	No
Security	Internal traffic may be unencrypted	End-to-end encrypted
5️⃣ System Design Considerations

Certificates: centralized on LB/CDN vs distributed on servers

Performance: offload expensive TLS handshake to LB/CDN

Security: internal traffic can be HTTPS (re-encrypt) or HTTP (trusted network)

Scalability: multiple servers behind LB can share single SSL termination

6️⃣ Example Flow with CDN / Load Balancer
Client --> CDN (SSL termination) --> Load Balancer (HTTPS or HTTP) --> Backend App


CDN terminates SSL at the edge → decrypts traffic

Load balancer may re-encrypt to backend

Backend receives plaintext HTTP (or HTTPS if re-encrypted)