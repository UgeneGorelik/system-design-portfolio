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
