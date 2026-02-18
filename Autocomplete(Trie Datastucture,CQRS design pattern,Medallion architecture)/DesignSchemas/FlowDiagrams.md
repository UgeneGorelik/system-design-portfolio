@startuml

actor User

component "Ingestion System" as Ingestion
component "Query System" as Query
database "Database" as DB

User --> Ingestion : Submit text / queries
Ingestion --> DB : Store & update data

User --> Query : Request autocomplete
Query --> DB : Fetch suggestions

@enduml



@startuml
actor User

component "Ingestion System" as Ingestion
database "Raw Search Requests (Bronze)" as Bronze
database "Individual Words Table (Silver)" as SilverWords
database "Dictionary Words Table (Silver)" as SilverDict
database "Word Count Table (Gold)" as Gold
component "Weighted Trie Generator" as TrieGen
component "Query System" as Query
database "Weighted Trie (In-Memory)" as TrieDB

' User writes
User --> Ingestion : Submit search query

' Ingestion stores raw data
Ingestion --> Bronze : Store raw search requests

' ETL / Rollup pipeline
Bronze --> SilverWords : Split raw strings into words
SilverWords --> SilverDict : Filter dictionary words
SilverDict --> Gold : Aggregate word counts
Gold --> TrieGen : Generate weighted trie
TrieGen --> TrieDB : Store in-memory trie

' Query path
User --> Query : Request autocomplete
Query --> TrieDB : Lookup suggestions
Query --> User : Return autocomplete results

@enduml
