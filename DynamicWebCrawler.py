import requests
from bs4 import BeautifulSoup

def web_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://facebook.com/kushalshm1'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('div',{'class': 'clearfix hasRightCol'}):
            href = link.get('href')
            print(href)
            page = page + 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div',{'class': 'clearfix hasRightCol'):
        print(item_name.string)
        href = 'http://www.facebook.com/kushalshm1'
        print(href)
get_single_item_data('https://facebook.com/kushalshm1')