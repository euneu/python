# website가 http://로 시작하지 않으면 http://로 시작하도록 만들기

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
    print(website)