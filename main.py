from bs4 import BeautifulSoup
import requests

url = "https://haberturk.com"

istek = requests.get(url)
htmlText=istek.text

print(htmlText)