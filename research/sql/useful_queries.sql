-- Low-budget cases
SELECT * FROM case_studies WHERE start_daily_budget <= 30 ORDER BY start_daily_budget, days;

-- All feed/title interventions
SELECT * FROM operator_events WHERE action_type LIKE '%TITLE%' OR action_type LIKE '%FEED%';

-- Sources with strongest evidence grades
SELECT * FROM sources WHERE evidence_grade IN ('A+','A','A-') ORDER BY source_id;

-- Google-related operator events
SELECT e.*, s.url FROM operator_events e JOIN sources s USING(source_id) WHERE e.action_type IN ('LAUNCH','RESTRUCTURE','SCALE','BIDDING','TITLE_TEST','MANUAL_TO_AUTOMATION','DO_NOT_THRASH');
