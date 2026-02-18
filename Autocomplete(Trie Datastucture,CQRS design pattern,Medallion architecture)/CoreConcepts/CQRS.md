Command Query Responsibility Segregation (CQRS)

CQRS is an architectural pattern that separates:

Commands → operations that change state (writes)

Queries → operations that read state (reads)

Instead of using the same model and database for both, CQRS splits them.

Core Idea

Use different models for updating data and reading data.

In traditional CRUD systems:

Same service
Same database
Same schema
Handles both reads and writes


In CQRS:

Write Model (Command Side)
↓
Read Model (Query Side)


They can:

Use different schemas

Use different databases

Scale independently

Optimize differently

Why CQRS Exists

In many real systems:

Read traffic >> Write traffic

Read queries need denormalized, optimized views

Write operations need strong consistency & validation