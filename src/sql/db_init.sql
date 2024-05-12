CREATE SCHEMA IF NOT EXISTS jobs;

SET search_path = jobs;

CREATE TABLE IF NOT EXISTS jobs (
  id SERIAL PRIMARY KEY,
  job_title VARCHAR(150) NOT NULL,
  company_name VARCHAR(100) NOT NULL,
  time_posted VARCHAR(50),
  num_applicants VARCHAR(50),
  description TEXT,
  seniority_level VARCHAR(100),
  employment_type VARCHAR(100),
  job_function VARCHAR(100),
  industries VARCHAR(100),
  created_on DATE NOT NULL DEFAULT CURRENT_DATE
);



