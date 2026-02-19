@startuml
actor User
participant CustomerApp
participant AuthService
participant CDN

== Login & Token Generation ==
User -> CustomerApp : Login(username/password)
CustomerApp -> AuthService : Validate credentials
AuthService --> CustomerApp : Access token
CustomerApp --> User : Signed CDN URL (token in query param)

== CDN Asset Request ==
User -> CDN : GET asset with signed URL
CDN -> AuthService : Validate token & permissions
AuthService --> CDN : Valid / Invalid
alt token valid
    CDN --> User : Return asset
else token invalid
    CDN --> User : Deny access
end

== Logout ==
User -> CustomerApp : Logout
CustomerApp -> AuthService : Invalidate token
@enduml


@startuml
actor User

' Components
component "API Gateway\n(rate limiting, logging)" as APIGW
component "Storage Service\n(assets)" as Storage
component "Metadata Service\n(file directories, storage hosts)" as Metadata
component "Secrets Management Service\n(encryption keys)" as Secrets
component "Origin Service\n(original asset source)" as Origin

' User request flow
User --> APIGW : Request asset

' API Gateway internal flow
APIGW --> Metadata : Lookup asset location
APIGW --> Storage : Retrieve asset
APIGW --> Secrets : Retrieve encryption key (if needed)

' Handle missing asset
APIGW --> Origin : Request missing asset
Origin --> Storage : Store asset
Origin --> Metadata : Update metadata
APIGW --> User : Return asset

@enduml


@startuml
title High-Level CDN Architecture

skinparam componentStyle rectangle
skinparam shadowing false

actor Users

component "API Gateway" as APIGW
component "Rate Limiting Service" as RateLimit
component "Logging Service" as Logging
component "Metadata Service" as Metadata
component "Storage Service" as Storage
component "Secrets Management Service" as Secrets
component "Origin Service" as Origin

Users --> APIGW : Request Asset

APIGW --> RateLimit : Check limits
APIGW --> Logging : Log request
APIGW --> Metadata : Lookup asset location

Metadata --> Storage : Get storage host/path
APIGW --> Storage : Fetch asset

APIGW --> Secrets : Retrieve encryption keys
Secrets --> Storage : Decrypt / Encrypt

APIGW --> Origin : Fetch if missing
Origin --> Storage : Store new asset
Origin --> Metadata : Update asset location

@enduml


@startuml
title Encrypted Asset Download (Cache Miss)

start

:Client sends request to API Gateway;

:Check rate limit;
if (Rate limit OK?) then (Yes)
else (No)
  :Reject request;
  stop
endif

:Fetch metadata from Metadata Service;
if (Asset found in CDN?) then (Yes)
  :Follow encrypted asset flow;
  stop
else (No)

  :Fetch asset from Origin Service;

  fork
    :Generate random encryption key;
    :Encrypt asset;
    :Store encrypted asset in Storage Service;
    :Store encryption key in Secrets Management Service;
    :Update metadata;
  fork again
    :Stream plaintext asset to Client;
  end fork

endif

stop
@enduml
