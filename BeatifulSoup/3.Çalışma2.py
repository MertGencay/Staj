import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("span", class_="titleline")

for i, title in enumerate(titles, start=1):
    link = title.find("a")
    print(f"{i}. {link.text}\n   {link['href']}\n")
