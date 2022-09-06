#이동한 다음 웹사이트를 가져옴
from requests import get
websites =(
    "google.com",
    "naver.com",
    "airbnb.com",
    "https://twitter.com",
    "https://facebook.com"
)

for website in websites :
    # not를 붙여줌으로써  if문이 false일 때로 설정
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    print(response.status_code)