System Design Portfolio
🚀 Purpose of This Repository

This repository documents my structured practice and exploration of large-scale system design.

The goal is to:

Develop deep intuition for distributed systems

Practice designing scalable, reliable architectures

Explore trade-offs between different technologies and patterns

Prepare for senior-level system design interviews

Build a public record of architectural thinking

Each system in this repository is treated as if it were a real production system — including requirements analysis, trade-offs, scaling strategies, and failure handling.

📂 Repository Structure

Each folder inside designs/ represents a complete system design.

Example:

designs/
  ├── url-shortener/
  ├── realtime-chat/
  ├── online-code-editor/
  └── event-driven-order-system/


Each system folder contains multiple files documenting the full design process.

📁 System Design Phases
01-requirements.md

Defines the problem and constraints.

This file clarifies:

What the system must do (functional requirements)

Performance, availability, and scale expectations (non-functional requirements)

It establishes boundaries before any architectural decisions are made.

02-entities.md

Defines the core domain model.

Identifies:

Primary objects in the system

Relationships between them

Persistent vs transient data

This step ensures clarity before designing APIs or storage.

03-api-design.md

Defines the external contract of the system.

Specifies:

Endpoints

Request/response formats

Authentication and authorization

Idempotency and validation rules

API design is completed before implementation details to ensure interface-first thinking.

04-database-design.md

Defines data storage strategy.

Includes:

Database choice rationale (SQL vs NoSQL)

Schema design

Indexing strategy

Partitioning / sharding plan

Data growth estimation

This document explains how the system persists and retrieves data at scale.

05-high-level-architecture.md

Defines system components and data flow.

Includes:

Major services

Infrastructure components

Caching layers

Messaging systems (if applicable)

Request lifecycle diagrams

This represents the first complete architectural view.

06-scaling-strategy.md

Explains how the system handles growth.

Covers:

Horizontal scaling

Load distribution

Hotspot mitigation

Caching strategies

Read/write separation

Multi-region considerations (if applicable)

This document stress-tests the architecture.

07-failure-scenarios.md

Analyzes resilience and fault tolerance.

Explores:

Node failures

Network partitions

Data inconsistencies

Retry strategies

Circuit breakers

Disaster recovery

This step evaluates system robustness under failure conditions.

08-tradeoffs.md

Documents architectural decisions and alternatives.

Explains:

Why specific technologies were chosen

Alternatives that were considered

Limitations of the chosen design

Future improvements

Each system is broken into explicit architectural phases to reflect real-world engineering workflows.

📁 /patterns

Reusable architecture building blocks referenced across system designs:

Event Sourcing

CQRS

Consistent Hashing

Rate Limiting

Circuit Breaker

Leader Election

Distributed Locking

CRDT vs OT

Write-through vs Write-back caching

And other distributed system patterns

This directory serves as a knowledge base for architectural decisions and recurring design components.


/infrastructure

This directory contains Infrastructure-as-Code (IaC) examples that demonstrate how selected system designs could be deployed in real-world environments.

The goal is to bridge architecture design with practical deployment strategies.

Example structure:

infrastructure/
  ├── serverless-url-shortener/
  │     ├── main.tf
  │     ├── variables.tf
  │     ├── outputs.tf
  │     └── README.md