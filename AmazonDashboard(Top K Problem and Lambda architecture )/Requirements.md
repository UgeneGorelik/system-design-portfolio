Functional Requirements

Top K Products Dashboard

Display the top-selling (and optionally worst-selling) products by sales volume.

Include both ranking and sales counts for the products.

Time Intervals

Support aggregation over configurable intervals: hour, day, week, year.

Approximate vs Accurate Results

Recent periods (last few hours): approximate rankings and volumes are acceptable.

Older periods: provide accurate counts and rankings.

Number of Products

Must support Top 10, but ideally allow querying arbitrary numbers of products.

Event Scope

Consider only initial sales events. Ignore refunds, exchanges, and recalls.

Tie Handling

For equal sales volumes, any item can be chosen (tie-breaking strategy is flexible).