
from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')

base_url = "https://www.indeed.com/jobs?q="
search_term = "python"

browser.get("https://naver.com")