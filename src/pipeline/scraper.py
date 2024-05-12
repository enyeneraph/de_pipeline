import requests
from bs4 import BeautifulSoup
import pandas as pd

    # #Get the HTML, parse the response and find all list items(jobs postings)
    # list_data = response.text


def scrape_job_details(job_url):
    job_response = requests.get(job_url)
    job_soup = BeautifulSoup(job_response.text, "html.parser")

    #  Create a dictionary to store job details
    job_post = {}
    
    # Extract  the job title
    try:
        job_post["job_title"] = job_soup.find("h1", class_="top-card-layout__title").text.strip()
    except:
        job_post["job_title"] = None
        
    # Extract the company name
    try:
        job_post["company_name"] = job_soup.find("a", class_="topcard__org-name-link").text.strip()
    except:
        job_post["company_name"] = None
        
    # Try to extract and store the time posted
    try:
        job_post["time_posted"] = job_soup.find("span", class_="posted-time-ago__text").text.strip()
    except:
        job_post["time_posted"] = None
        
    # Extract the number of applicants
    try:
        job_post["num_applicants"] = job_soup.find("figcaption", class_= "num-applicants__caption").text.strip()
    except:
        job_post["num_applicants"] = None

    # Extract job description
    try:
        job_post["description"] = job_soup.find("div", class_="show-more-less-html__markup").text.strip()
    except:
        job_post["description"] = None

    # Extract additional job tags
    try:
        keys_ = job_soup.find_all("li", class_="description__job-criteria-item")
        job_post.update({key_.find('h3').text.strip():key_.find('span').text.strip() for key_ in keys_ })
    except Exception as e:
        print(e)
    
    result = {k.replace(' ','_').lower():v for k, v in job_post.items()}
    return result


def scrape_single_page(url):
    response = requests.get(url)

    #Get the HTML, parse the response and find all list items(jobs postings)
    list_data = response.text
    list_soup = BeautifulSoup(list_data, "html.parser")
    page_jobs = list_soup.find_all("li")
    

    link_list = []

    #Iterate through job postings to find job links
    for job in page_jobs:
        try:
            link = job.find("a", class_="base-card__full-link").get("href")
            link_list.append(link)
        except:
            pass
    job_list = []

    for index,job_url in enumerate(link_list):
        job_post = scrape_job_details(job_url=job_url)
        job_list.append(job_post)
        print(f"completed: {index}")

    return job_list



def scrape_multiple_pages():

    data = []
    page_num = 0
    for page_num in range(0,1):
        print(f"Scraping data for page {page_num}")
        url = f"https://www.linkedin.com/jobs/search?keywords=Data%2BEngineer&trk=public_jobs_jobs-search-bar_search-submit&pageNum={page_num}"
        page_data = scrape_single_page(url)
        data.extend(page_data)

    return data
