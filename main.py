import urllib.request
import json
from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://google.com/search?q=Wadapav'

# Perform the request
request = urllib.request.Request(url)

# Set a normal User Agent header
request.add_header(
    'User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
raw_response = urllib.request.urlopen(request).read()

# Read the repsonse as a utf-8 string
html = raw_response.decode("utf-8")

soup = BeautifulSoup(html, 'lxml')

all_links = []

for result in soup.select('.tF2Cxc')[:5]:
    title = result.select_one('.DKV0Md').text
    link = result.select_one('.yuRUbf a')['href']

    all_links.append(link)


with open('out.txt', 'w', encoding="utf-8") as f:
    for current in all_links:
        print(current)
        html_text = requests.get(current).text
        soup = BeautifulSoup(html_text, 'lxml')

        detail = soup.find_all('p')

        f.write(current)
        if detail:
            for desc in detail:
                i = desc.text
                f.write(i)
                f.write('\n')
