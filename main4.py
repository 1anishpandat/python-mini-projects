import requests

query = "ai"
api = "bdb8ecee4532434cb89eaf1279c2a33d"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-02-08&sortBy=publishedAt&apiKey={api}"
print(url)
c = requests.get(url)
data = c.json()

articles = data["articles"]
for article in articles:
    print(article["title"])
    print(article["url"])
    print("\n****************************************\n")
