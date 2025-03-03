import requests
from bs4 import BeautifulSoup
import json

url = "https://www.imdb.com/chart/top/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract JSON data
    script = soup.find("script", {"type": "application/ld+json"})
    data = json.loads(script.string)

    # Extract movie list from HTML
    movies = soup.find_all('li', class_='ipc-metadata-list-summary-item')

    for i in range(10):  # Get top 10 movies
        title = movies[i].find('h3', class_='ipc-title__text').text
        year = movies[i].find('span', class_='sc-d5ea4b9d-7').text
        summary = data["itemListElement"][i]["item"].get("description", "Summary not available")

        print(f"{title}")
        print(f"Year: {year}")
        print(f"Summary: {summary}")
        print("-" * 30)

else:
    print("Failed to access the page")
