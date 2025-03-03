import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = "https://en.wikipedia.org/wiki/Sachin_Tendulkar"

# Send a GET request to the webpage and gives html content and other attributes
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image tags (<img>) in the HTML
image_tags = soup.find_all('img')

# Extract and display the 'src' attribute of each image tag
for img in image_tags:
    src = img.get('src')
    if src:  # Ensure the 'src' attribute exists
        print(src)
