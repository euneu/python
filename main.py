#이동한 다음 웹사이트를 가져옴
from requests import get
websites =(
    "google.com",
    "https://httpstat.us/502",
    "https://httpstat.us/404",
    "https://httpstat.us/300",
    "https://httpstat.us/200",
    "https://httpstat.us/101"
)

#웹사이트의 http 상태를 받을 딕셔너리
results ={}

for website in websites :
    # not를 붙여줌으로써  if문이 false일 때로 설정
    #웹사이트가 hppts://로 시작하지 않으면 문자를 붙여
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    code = response.status_code
    if code >= 100 and code < 200:
        results[website] = "1xx/impormation responses"
    elif code >= 200 and code < 300:
        results[website] = "2xx/Successful"
    elif code >= 300 and code < 400:
        results[website] = "3xx/Redirection"
    elif code >= 400 and code < 500:
        results[website] = "4xx/Client error"
    elif code >= 500 and code < 600:
        results[website] = "5xx/Server error"

print(results)