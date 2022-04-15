from bs4 import BeautifulSoup
import requests

html_text = requests.get(
    'https://www.reuters.com/technology/twitter-adopts-poison-pill-fight-musk-2022-04-15/').text
soup = BeautifulSoup(html_text, 'lxml')
info = soup.find(
    'div', class_='article-body__content__3VtU3 paywall-article')
detail = info.find_all(
    'p', class_='text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__large__nEccO body__base__22dCE body__large_body__FV5_X article-body__element__OOj6H')
for desc in detail:
    i = desc.text
    print(i)
    print('')
