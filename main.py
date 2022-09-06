#이동한 다음 웹사이트를 가져옴
from requests import get
websites =(
    "google.com",
    "naver.com",
    "airbnb.com",
    "https://twitter.com",
    "https://facebook.com"
)

#웹사이트의 http 상태를 받을 딕셔너리
results ={}

for website in websites :
    # not를 붙여줌으로써  if문이 false일 때로 설정
    #웹사이트가 hppts://로 시작하지 않으면 문자를 붙여
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
        results[website] = "OK"
    else :
        results[website] = "FAILED"

print(results)