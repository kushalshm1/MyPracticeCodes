import requests
from bs4 import BeautifulSoup

def web_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://facebook.com/kushalshm1'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',{'class': 'clearfix hasRightCol'}):
            href = link.get('href')
            print(href)
            page = page + 1

web_spider(1)
