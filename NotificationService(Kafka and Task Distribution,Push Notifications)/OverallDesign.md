Design a system that:

Sends notifications/alerts to users

Email, SMS, push notifications, in-app notifications

Supports real-time delivery (WebSockets or push)

Handles high throughput and bursts

Guarantees delivery (eventual or at-least-once)

Allows filtering / subscription preferences

Scalable and highly available

🏗 High-Level Architecture

Core components:

Client (Web/Mobile/App)

API Gateway

Notification Service

Handles notification creation and routing

Message Queue / Event Bus (Kafka, RabbitMQ, SQS)

Delivery Workers / Push Workers

Email, SMS, Push, In-App, WebSocket

User Preferences / Subscription Service

Cache / Session Store (for WebSocket connections)

Database (persistent notification store)

Monitoring / Logging

🔁 Notification Flow
1️⃣ Write Path (Create Notification)

Client or internal service → API Gateway

API Gateway → Notification Service

Notification Service:

Validates request

Checks user subscription/preferences

Writes notification metadata to DB (persistent)

Push notification event to Message Queue / Event Bus

2️⃣ Delivery Path (Asynchronous)

Delivery Worker consumes event from queue

Checks delivery channel:

Push / WebSocket → check session store for connected sockets → send in real-time

Email / SMS → enqueue for external provider (SES, Twilio, etc.)

Update delivery status in DB

If failed → retry (exponential backoff)

🧠 Real-Time Delivery Options
1️⃣ WebSockets

Persistent connection for instant notifications

Store connection info in Redis / in-memory session store

Worker pushes notification → socket → client

2️⃣ Server-Sent Events (SSE)

Simpler, one-way channel

Good for browser dashboards

3️⃣ Push Notifications (Mobile)

APNs (iOS), FCM (Android)

Worker sends via provider API



Push New Alert Flow
Step 1: Create / Push Alert

Some producer creates the alert. Could be:

Your app backend (order shipped, price drop, message received)

Admin system (system maintenance alert)

API Gateway / Notification Service receives it.

Notification metadata (user ID, message, channel, timestamp, etc.) is pushed to a queue.

Why push to a queue?

Decouples alert creation from delivery

Supports bursts of notifications

Enables retries / failure handling

Workers can scale independently

Step 2: Queue Storage

Queue could be:

Kafka → durable, partitioned, high throughput

RabbitMQ / SQS → simple queue, good for at-least-once delivery

Queue stores the alert until a consumer pulls it

Step 3: Delivery Worker (Consumer)

One or more workers pull messages from the queue.

Worker determines delivery channel (WebSocket, Push, SMS, Email).

Worker Actions per Message:

Check user subscription / preferences

Deliver the notification:

WebSocket → lookup user session in Redis → send

Push → send to FCM / APNs

Email / SMS → send via external provider

Update notification status in database (sent / failed)

On failure, retry with exponential backoff or send to dead-letter queue

Step 4: Delivery

Client receives the alert in near-real-time (WebSocket/push) or asynchronously (email/SMS).

Worker continues to pull messages from the queue until empty.