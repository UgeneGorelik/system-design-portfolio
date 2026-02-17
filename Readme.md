# 🏗 System Design Portfolio

## 🚀 Purpose

This repository documents structured exploration and practice of large-scale system design.

Goals:

- Develop intuition for distributed systems  
- Design scalable, reliable architectures  
- Explore trade-offs between technologies and patterns  
- Evaluate failure scenarios and robustness  
- Prepare for senior-level system design interviews  
- Build a public record of architectural thinking  

Each system is treated as a real production system, including requirements analysis, scaling strategy, trade-offs, and failure handling. This repository focuses on architectural reasoning rather than production-ready implementation.

---

## 📂 Repository Structure

### `/designs`

Each folder represents a complete system design.  

Example:

designs/
├── url-shortener/
├── realtime-chat/
├── online-code-editor/
└── event-driven-order-system/


Each system contains multiple files documenting the full design process, broken into explicit architectural phases.

---

## 📐 System Design Phases

### 01 — Requirements
Defines problem and constraints:

- Functional requirements  
- Non-functional requirements (performance, availability, scale)  
- Scope boundaries  

### 02 — Entities
Defines core domain model:

- Primary objects  
- Relationships  
- Persistent vs transient data  

### 03 — API Design
Defines external system contract:

- Endpoints  
- Request/response formats  
- Authentication & authorization  
- Idempotency and validation rules  

### 04 — Database Design
Defines storage strategy:

- SQL vs NoSQL rationale  
- Schema design  
- Indexing  
- Partitioning/sharding  
- Data growth estimation  

### 05 — High-Level Architecture
Defines components and data flow:

- Major services  
- Infrastructure components  
- Caching layers  
- Messaging systems (if applicable)  
- Request lifecycle diagrams  

### 06 — Scaling Strategy
Explains handling of growth:

- Horizontal scaling  
- Load distribution  
- Hotspot mitigation  
- Read/write separation  
- Caching strategies  
- Multi-region considerations  

### 07 — Failure Scenarios
Analyzes resilience:

- Node failures  
- Network partitions  
- Data inconsistencies  
- Retry strategies  
- Circuit breakers  
- Disaster recovery  

### 08 — Trade-offs
Documents architectural decisions:

- Technology choices and rationale  
- Alternatives considered  
- Limitations of design  
- Future improvements  

---

## 🧩 `/patterns`
Reusable architecture building blocks:

- Event Sourcing  
- CQRS  
- Consistent Hashing  
- Rate Limiting  
- Circuit Breaker  
- Leader Election  
- Distributed Locking  
- CRDT vs OT  
- Write-through vs Write-back caching  

---

## 🏗 `/infrastructure`
Infrastructure-as-Code (IaC) examples for deploying designs:

infrastructure/
├── serverless-url-shortener/
│ ├── main.tf
│ ├── variables.tf
│ ├── outputs.tf
│ └── README.md



Bridges architecture with real-world deployment.

---

## 🧠 Architectural Principles

- Horizontal scalability  
- Clear service boundaries  
- Separation of read/write paths  
- Event-driven patterns where appropriate  
- Eventual consistency when acceptable  
- Failure-aware design  
- Observability-first mindset  
- Explicit trade-off documentation  

---

## 🚀 How to Navigate

1. **Start with Requirements** – Read `Requirements.md` to understand system scope, scale assumptions, latency and availability goals, and constraints.  
2. **Review High-Level Architecture** – See `HLDDiagram.png` and `OverallDesign.md` to understand core components, service boundaries, read/write separation, storage decisions, scaling approach, and trade-offs.  
3. **Explore Subsystems** – Dive deeper into:
   - `Db-Schema.md` → Database modeling  
   - `Caching_and_Cdn.md` → Cache layers and CDN strategy  
   - `Api.md` → Public API design  
   - `FlowDiagrams.md` → Request lifecycle breakdown  
   - `MonitoringAlerting.md` → Observability and alerting planning  
4. **Event-Driven Variant** – Optional asynchronous design with queue-based ingestion: see `OptionalHldWithKafka.png`.  
5. **Run Minimal Backend Example (Optional)** – For demonstration purposes:
   - Requirements: Python 3.9+  
   - Run locally:  
     ```bash
     python server_code_simple_example.py
     ```  
   - Deploy via Serverless (if AWS credentials configured):  
     ```bash
     npm install -g serverless
     serverless deploy
     ```  

---

## 🎯 Intended Use

This repository is intended for:

- System design interview preparation  
- Portfolio demonstration of architectural thinking  
- Reference for scalable backend patterns  
- Structured approach to distributed systems  

---
