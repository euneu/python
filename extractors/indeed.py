from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver

def get_page_count(keyword):
    browser = webdriver.Chrome('./chromedriver.exe')
    base_url = "https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = (soup.find("ul", class_="pagination-list"))
    if pagination == None :
        return 1
    pages = pagination.find_all("li",recursive=False)
    count = len(pages)
    if count >= 5 :
        return 5
    else :
        count


def extra_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages) :
        browser = webdriver.Chrome('./chromedriver.exe')
        base_url = "https://kr.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting", final_url)
        browser.get(final_url)

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
                    'company' : company.string.replace(",", " "),
                    'location' : location.string.replace(",", " "),
                    'position' : title.replace(",", " ")
                }
                results.append(job_data)
    return results        
