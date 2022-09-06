websites =(
    "google.com",
    "naver.com",
    "airbnb.com",
    "https://twitter.com",
    "https://facebook.com"
)

for website in websites :
    if website.startswith("https://"):
        print("good to go")
    else :
        print("we have to fix")