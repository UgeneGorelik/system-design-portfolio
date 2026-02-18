Concept: Bronze / Silver / Gold Tables (Medallion Architecture)

This is a common data lake / lakehouse pattern:

Layer	Purpose	Data Quality	Examples
Bronze	Raw ingestion	Raw, uncleaned, duplicated	Logs, clickstream, raw JSON
Silver	Cleaned, enriched	Deduplicated, validated, typed	Filtered logs, parsed events, user profiles
Gold	Aggregated, curated	Business-ready, aggregated	Daily metrics, KPIs, dashboards, summary tables
Flow
Raw Data → Bronze → Silver → Gold


Bronze: “just land the data”

Silver: “clean and standardize”

Gold: “aggregate & optimize for analytics”

2️⃣ Roll-Up Jobs

Roll-up jobs are scheduled or streaming processes that aggregate data over time to make it smaller, faster to query, and ready for reporting.

Typical roll-ups:

Summing counts per day/week/month

Average/min/max values

Top-K users, products, etc.

Example:

Raw clickstream: millions of events per day → Bronze table

Cleaned clicks: deduplicated & typed → Silver table

Aggregated metrics: daily clicks per product → Gold table

Example Tables

Bronze Table (Raw Clicks)

event_id	user_id	product_id	timestamp	raw_data
1	101	A123	2026-02-18 09:01	{...}
2	102	B456	2026-02-18 09:02	{...}

Silver Table (Cleaned Events)

event_id	user_id	product_id	event_type	timestamp
1	101	A123	click	2026-02-18 09:01
2	102	B456	view	2026-02-18 09:02

Gold Table (Aggregated Metrics)

date	product_id	total_clicks	total_views
2026-02-18	A123	1500	3200
2026-02-18	B456	900	2000