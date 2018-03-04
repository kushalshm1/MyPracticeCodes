import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".png"
    urllib.request.urlretrieve(url, full_name)

download_web_image("http://www.unixstickers.com/image/cache/data/stickers/python/python_sh-600x600.png")