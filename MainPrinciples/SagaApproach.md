1️⃣ Saga Pattern

Definition:
A sequence of local transactions where each transaction updates its service and publishes an event or triggers the next transaction.

If something fails, compensating transactions are executed to undo previous steps.

Ensures eventual consistency.

2️⃣ Orchestration Approach

Definition:

A central coordinator (Saga Orchestrator) controls the workflow.

Orchestrator tells each service what to do next, including compensations.

Example: Airbnb booking

Orchestrator → Create Reservation

Orchestrator → Charge Payment

Orchestrator → Reserve Inventory

If any step fails → Orchestrator triggers compensating transactions

Pros

Clear central control

Easier debugging and monitoring

Explicit compensation

Cons

Single coordination point → potential bottleneck

Services tightly coupled to orchestrator

Mental model: Imperative workflow

do A
if success do B
if success do C
else compensate

3️⃣ Choreography Approach

Definition:

No central coordinator.

Services communicate via events, reacting to what other services emit.

Example:

Order Service emits "ReservationCreated"

Payment Service listens → charges → emits "PaymentCompleted"

Inventory Service listens → reserves → emits "InventoryReserved"

Failure → services emit compensating events

Pros

Highly decoupled

Scales naturally

Services are autonomous

Cons

Harder to debug global flow

Event ordering / reliability can be complex

Implicit workflow → harder to reason about

Mental model: Event-driven chain reaction

A emits event → B reacts → C reacts → ...

4️⃣ Comparison Table
Dimension	Orchestration	Choreography
Control Flow	Central	Distributed / event-driven
Coupling	Higher (services follow orchestrator)	Lower (services autonomous)
Observability	Easier (central coordinator)	Harder (must trace events)
Debugging	Easier	Complex
Scalability	Limited by orchestrator	Highly scalable
Complexity Type	Centralized workflow logic	Emergent distributed behavior
Compensations	Explicit, coordinated	Implicit via events
5️⃣ When to Use Which

Orchestration:

Complex business workflows

Strict ordering required

Strong visibility and monitoring needed

Example: Financial transactions, booking systems

Choreography:

Highly decoupled microservices

Event-driven architecture

Workflows are simple or event-based

Example: E-commerce microservices updating stock, emails, recommendations