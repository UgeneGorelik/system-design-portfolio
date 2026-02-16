User ->relational sql 
Column	Type	Notes
id	PRIMARY KEY	Unique user identifier
first_name	text	Optional
last_name	text	Optional
signup_ts	integer	Timestamp of account creation

Users are minimal; authentication handled separately.

2️⃣ Post-> non relation db maybe dynamo
Column	Type	Notes
id	PRIMARY KEY	Unique post ID
created_at	integer	Post creation timestamp
poster_id	integer	FK to User.id
location_id	integer	Optional reference for location metadata
title	text	Post title
description	text	Post content
price	integer	Optional price field
condition	text	Item condition
country_code	char(2)	ISO country code
state	text	State/region
city	text	City/locality
street_number	integer	Optional
street_name	text	Optional
zip_code	text	Optional
phone_number	integer	Optional contact
email	text	Optional contact