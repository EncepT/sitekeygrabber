__author__ = "Nico Holubek / Shiba "


from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time
import pyperclip

def grab_sitekey():
    captcha_url = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36' '(KHTML, like Gecko) Chrome/56.0.2924.28 Safari/537.36'})
    product_url = urlopen(captcha_url)
    soup = BeautifulSoup(product_url, 'html.parser')
    sitekey = soup.find('div', attrs={'class': 'g-recaptcha'})['data-sitekey']
    print("Grabbing sitekey..")
    time.sleep(1)
    print(sitekey)
    time.sleep(0.5)
    pyperclip.copy(sitekey)
    print("Copied to clipboard")
    time.sleep(0.5)
    print("Enjoy ;)")

url = input("Enter a url to an adidas product with an Captcha : ")

grab_sitekey()
