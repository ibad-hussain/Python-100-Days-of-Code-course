# EXERCISE 10 - NEWS APP
# Problem Statement: Use the NewsAPI and the requests module to fetch the daily news related to different topics.
  # Go to: https://newsapi.org/ and explore the various options to build you application.



import requests
import json

while True:
    query = input("What type of news are you interested in ? (enter 0 to exit) : ")
    
    if query == "0":
      break

    url = f"https://newsapi.org/v2/everything?q={query}&from=2024-09-02&sortBy=publishedAt&apiKey=1bfa2c3570f74297a6e3c58a5bf92d65"
    r = requests.get(url)
    news = json.loads(r.text)
    
    if 'articles' in news:
      for article in news["articles"]:
        print("------------------")
        print("Titile: ", article["title"])
        print("Description: ", article["description"])
        print("------------------")
    else:
        print("No articles found for your query. Please try again.!")