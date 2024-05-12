COPY
(SELECT * FROM jobs.jobs
WHERE created_on = CURRENT_DATE)
TO '/tmp/new_jobs.csv' DELIMITER ',' CSV HEADER;