[Producer / API] 
       |
       v
   Notification Queue   <-- push new alert
       |
       v
Delivery Workers / Consumers  <-- pull from queue
       |
       v
Delivery Channels:
    - WebSocket -> Client
    - Push (FCM/APNs)
    - Email / SMS
       |
       v
Update DB (status)




plantuml

@startuml
title Notification / Alerting Service Flow

actor Client

participant "API / Notification Service" as API
participant "Notification Queue" as Queue
participant "Delivery Worker" as Worker
participant "WebSocket / Session Store" as WS
participant "Push Provider (FCM/APNs)" as Push
participant "Email/SMS Provider" as Email
database "Notification DB" as DB

== Create Notification ==
Client -> API : Send new alert
API -> Queue : Push alert to queue
API -> DB : Save notification metadata

== Delivery ==
Worker -> Queue : Pull alert
Worker -> DB : Update status (processing)
alt WebSocket connected
