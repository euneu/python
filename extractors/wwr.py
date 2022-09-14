from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?&term="
    

    response = get(f"{base_url}{keyword}")

    if response.status_code!= 200:
        print("Can't request website")
    else :
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs")
        # 모든 li 찾아서 job_posts에 저장
        for job_section in jobs :
            job_posts = job_section.find_all('li')
            # li 항목 중에 view_all이라는 항목을 보고 싶지 않음
            # 그리고 그 항목이 맨 마지막에 존재하므로 pop으로 없애버림
            #- <- 이건 뒤에서 시작이라는 뜻
            job_posts.pop(-1)
            for post in job_posts :
                # a태그를 가져올 건데 두번째만 저장할 것
                anchors = post.find_all('a')
                anchors = anchors[1]
                link = anchors['href']
                company, kind, region = anchors.find_all('span', class_="company")
                title = anchors.find('span', class_='title')
                job_data = {
                    'link' : f"https://weworkremotely.com{link}",
                    'company' : company.string.replace(",", " "),
                    'location' : region.string.replace(",", " "),
                    'position' : title.string.replace(",", " ")  
                }
                results.append(job_data)
        return results            
