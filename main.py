from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

browser.get(f"{base_url}{search_term}")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = (soup.find("ul", class_="jobsearch-ResultsList"))
jobs = job_list.find_all('li', recursive=False)
print(len(jobs))
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None :
        print("job li")
    else :
        print("mosaic li")
