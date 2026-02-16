@startuml
title Craigslist-Style System with GeoDNS 
actor "User / Client" as Client

rectangle "GeoDNS / Regional Routing" as GeoDNS

rectangle "Backend / API Server" as Backend {
  rectangle "Post Management"
  rectangle "User Management"
  rectangle "Reporting / Moderation"
}

database "SQL Database (Regional Replica)" as SQLDB
rectangle "Cache Layer (Optional)" as Cache
cloud "Object Store / CDN (Images)" as ObjectStore

' User request flow
Client --> GeoDNS : Request (browse / post / report)
GeoDNS --> Backend : Route to nearest regional server

' Backend interactions
Backend --> SQLDB : Read / Write Posts, Users, Reports
Backend --> Cache : Read / Write hot posts
Backend --> ObjectStore : Upload / Retrieve images

' Responses
SQLDB --> Backend : Query results
Cache --> Backend : Cached data
ObjectStore --> Backend : Image URLs

Backend --> Client : API Response (JSON + image URLs)

@enduml


optional

@startuml
title Craigslist-Style System with GeoDNS and Kafka

' Layout left-to-right for cleaner arrows
left to right direction

' Components
rectangle "User / Client" as Client
rectangle "GeoDNS / Regional Routing" as GeoDNS
rectangle "Backend / API Server" as Backend {
  rectangle "Post Management"
  rectangle "User Management"
  rectangle "Reporting / Moderation"
}
database "SQL Database (Regional Replica)" as SQLDB
rectangle "Cache Layer (Optional)" as Cache
rectangle "Object Store / CDN (Images)" as ObjectStore
rectangle "Event Queue (Kafka)" as Kafka

' User request flow
Client -right-> GeoDNS : Request (browse / post / report)
GeoDNS -right-> Backend : Route to nearest regional server

' Backend interactions
Backend -down-> SQLDB : Read / Write Posts, Users, Reports
Backend -down-> Cache : Read / Write hot posts
Backend -down-> ObjectStore : Upload / Retrieve images
Backend -down-> Kafka : Send posts asynchronously
Kafka -up-> Backend : Async processing / notifications

' Responses back to client
SQLDB -up-> Backend : Query results
Cache -up-> Backend : Cached data
ObjectStore -up-> Backend : Image URLs
Backend -left-> Client : API Response (JSON + image URLs)

@enduml
