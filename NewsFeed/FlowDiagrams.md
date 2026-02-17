@startuml
title Simple News Feed Architecture

actor User
actor Client as "Content Client"

component "API Gateway" as APIGW
component "Backend1 (Feed API)" as Backend1
component "Cache (Redis)" as Cache
component "Metadata System" as Metadata
component "HDFS (News Storage)" as HDFS

component "News Ingestion Service" as Ingestion
component "Moderation Service" as Moderator
queue "Message Queue" as Queue
component "Backend2 (Async Processor)" as Backend2

' =========================
' Read Path
' =========================
User --> APIGW
APIGW --> Backend1
Backend1 --> Cache
Backend1 --> Metadata
Backend1 --> HDFS

' =========================
' Write Path
' =========================
Client --> Ingestion
Ingestion --> Moderator
Moderator --> Queue
Backend2 --> Queue : polls
Backend2 --> HDFS
Backend2 --> Metadata

@enduml














@startuml
title News Feed Architecture (Pretty Version)

skinparam componentStyle rectangle
skinparam shadowing true
skinparam ArrowColor #1F77B4
skinparam ActorBorderColor #FF6600
skinparam ActorFontColor #FF6600
skinparam componentBorderColor #333333
skinparam componentBackgroundColor #EEEEEE

' =========================
' Actors
' =========================
actor User #FFCC00
actor Client as "Content Client" #FFCC00

' =========================
' API Layer
' =========================
rectangle "API Layer" {
    component "API Gateway" as APIGW #B2DFDB
    component "Backend1 (Feed API)" as Backend1 #B2DFDB
}

' =========================
' Cache & DB Layer
' =========================
rectangle "Cache & Database" {
    component "Redis Cache\n(precomputed feeds & metadata)" as Cache #AED581
    component "Distributed SQL\n(Zookeeper-managed)" as DistSQL #AED581
    component "Metadata System" as Metadata #AED581
}

' =========================
' Storage Layer
' =========================
rectangle "Storage Layer" {
    component "HDFS (News Storage)" as HDFS #FFCCBC
}

' =========================
' ETL Layer
' =========================
component "Feed Preparation / ETL" as ETL #FFF176

' =========================
' Media Layer
' =========================
rectangle "Media Layer" {
    component "Media Service" as Media #90CAF9
    component "CDN" as CDN #90CAF9
}

' =========================
' Ingestion / Async Layer
' =========================
rectangle "Ingestion & Processing" {
    component "News Ingestion Service" as Ingestion #F48FB1
    component "Moderation Service" as Moderator #F48FB1
    queue "Message Queue" as Queue #F48FB1
    component "Backend2 (Async Processor)" as Backend2 #F48FB1
}

' =========================
' Read Path
' =========================
User --> APIGW
APIGW --> Backend1
Backend1 --> Cache : fetch precomputed feed & metadata
Backend1 --> ETL : fallback if cache miss
ETL --> HDFS : read raw posts
Backend1 --> Media : fetch media URLs
Media --> CDN : serve media via CDN
User --> CDN : fetch media directly

' =========================
' Write Path
' =========================
Client --> Ingestion
Ingestion --> Moderator
Moderator --> Queue
Backend2 --> Queue : polls
Backend2 --> HDFS
Backend2 --> Metadata
Backend2 --> ETL : triggers feed precompute
Client --> Media : upload media
Media --> CDN : publish media for fast delivery
Backend2 --> DistSQL : update metadata

@enduml
