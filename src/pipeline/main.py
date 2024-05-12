from pipeline.scraper import scrape_multiple_pages
from pipeline.ingest import insert_data, fetch_data, connect_db
import os

user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
port = os.environ["DB_PORT"]
host = os.environ["DB_HOST"]
db_name = os.environ["DB_NAME"]

def main():
    data = scrape_multiple_pages()
    for row in data:
        job_title, company_name = row['job_title'], row['company_name']

        conn = connect_db(user=user, password=password, host=host, database=db_name, port=port)
        query ="""select * from jobs.jobs where job_title = %s and company_name = %s"""
        values = (job_title, company_name)

        entry = fetch_data(conn, query, values)
        if entry is None:
            try:
                print(f"Job post for {job_title} by {company_name} does not exist :: Inserting data")
                insert_data(conn=conn, row=row)
            except Exception as e:
                print(e)

        else:
            print(f"Job post for {job_title} by {company_name} exists")


