#!/bin/bash
PGPASSWORD=${DB_PASSWORD} psql -h ${DB_HOST} -p ${DB_PORT} -U ${DB_USER} -d ${DB_NAME} -c "\copy (SELECT * FROM jobs.jobs
WHERE created_on = CURRENT_DATE) TO /opt/airflow/src/files/new_jobs.csv WITH DELIMITER ',' CSV HEADER"
