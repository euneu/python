from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

browser.get(f"{base_url}{search_term}")

results = []
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = (soup.find("ul", class_="jobsearch-ResultsList"))
jobs = job_list.find_all('li', recursive=False)
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None :
        # h2 = job.find("h2", class_="jobTitle")
        # a = h2.find("a")
        anchor = job.select_one("h2 a")

        #BeaurifulSoup이 자동으로 딕셔너리나 리스트로 만들어주기 때문에 이런식으로 데이터를 다루는 것이 가능함
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data ={
            'link' : f"https://kr.indeed.com{link}",
            'company' : company.string,
            'location' : location.string,
            'position' : title
        }
        results.append(job_data)
for result in results :
    print(result, "\n-----------------")
    