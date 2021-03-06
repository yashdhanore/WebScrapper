import urllib.request
import json
from bs4 import BeautifulSoup
import lxml
import requests

search_query = input("input search query: ")

search_query = search_query.replace(" ", "+")

# keywords that need to be looked for in the content
keywords = []

url = 'https://google.com/search?q='+search_query

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
    for current_link in all_links:
        # print(current_link)
        html_text = requests.get(current_link).text
        soup = BeautifulSoup(html_text, 'lxml')

        detail = soup.find_all('p')

        f.write(current_link)
        if detail:
            for desc in detail:
                text = desc.text
                # look for keywords if keywords list is not empty else dont
                if keywords:
                    for word in keywords:
                        if word in text:
                            f.write(text)
                else:
                    f.write(text)

                f.write('\n')
