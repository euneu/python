from extractors.indeed import extra_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("what do you want to search for?")

#두 개 다 리스트를 리턴함
indeed = extra_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed+ wwr

for job in jobs :
    print(job)
    print("-------------------")