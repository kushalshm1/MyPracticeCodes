import requests #it connects your code to internet
from bs4 import BeautifulSoup   #it gives it access to crawl websites
from crawler import Crawler
from tkinter import *

root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Web Crawler | Kushal Sharma")
mainloop()

def trade_spider(max_pages): #Main function and we will supply no of pages in it and it will crawl all the pages we supplied
    page = 2 #Variable that stores page numbers

    while page <= max_pages:
        url = 'http://oceanoffgames.com/page/' + str(page) #URL of the page we are gonna crawl
        source_code = requests.get(url) #Each time it loops it will connect to that page and stores the reault in source code
        plain_text = source_code.text #It going to take the text of this request; all the crap that we need to crawl
        soup = BeautifulSoup(plain_text) #Beautiful soup object; Example: Find all the titles in 'soup'
        for link in soup.findAll('h1', {'class':'title'}): #This paramaeer is ging to source code and find all the parameters
            #Now title class has got a lot of crap and we only want URL and Title
            href = link.get('href')
            print(href)
            page = page + 1

trade_spider(1)


crawler = Crawler()
crawler.crawl('http://techcrunch.com/')
# displays the urls
print(crawler.content['techcrunch.com'].keys())