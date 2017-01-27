from bs4 import BeautifulSoup
import requests
import sys
import time
import pyperclip

__author__ = "EncepT / Shiba "


assci = """
     _ _       _                _____           _     _                 _             _____                     _         __  _____ _     _ _           
    (_) |     | |              |  __ \         | |   | |               | |           |  ___|                   | |       / / /  ___| |   (_) |          
 ___ _| |_ ___| | _____ _   _  | |  \/_ __ __ _| |__ | |__   ___ _ __  | |__  _   _  | |__ _ __   ___ ___ _ __ | |_     / /  \ `--.| |__  _| |__   __ _ 
/ __| | __/ _ \ |/ / _ \ | | | | | __| '__/ _` | '_ \| '_ \ / _ \ '__| | '_ \| | | | |  __| '_ \ / __/ _ \ '_ \| __|   / /    `--. \ '_ \| | '_ \ / _` |
\__ \ | ||  __/   <  __/ |_| | | |_\ \ | | (_| | |_) | |_) |  __/ |    | |_) | |_| | | |__| | | | (_|  __/ |_) | |_   / /    /\__/ / | | | | |_) | (_| |
|___/_|\__\___|_|\_\___|\__, |  \____/_|  \__,_|_.__/|_.__/ \___|_|    |_.__/ \__, | \____/_| |_|\___\___| .__/ \__| /_/     \____/|_| |_|_|_.__/ \__,_|
                         __/ |                                                 __/ |                     | |                                            
                        |___/                                                 |___/                      |_|                                                                                                    
"""


enjoyassci = """
 _____      _                   __  
|  ___|    (_)               _  \ \ 
| |__ _ __  _  ___  _   _   (_)  | |
|  __| '_ \| |/ _ \| | | |       | |
| |__| | | | | (_) | |_| |   _   | |
\____/_| |_| |\___/ \__, |  ( )  | |
          _/ |       __/ |  |/  /_/ 
         |__/       |___/         
"""

print(assci)

US_link = ('http://www.adidas.com/us/shoes', 'US')
UK_link = ('http://www.adidas.co.uk/shoes', 'UK')
AU_link = ('http://www.adidas.com.au/shoes', 'AU')
CA_link = ('http://www.adidas.ca/shoes', 'CA')
SE_link = ('http://www.adidas.se/senaste', 'SE')
DE_link = ('http://www.adidas.de/schuhe', 'DE')
FR_link = ('http://www.adidas.fr/chaussures', 'FR')
country_link_list = [US_link, UK_link, AU_link, CA_link, SE_link, DE_link, FR_link]


def adidas_country():
    country = input('Which region you would like to have?  -  US, CA, AU, SE, DE, FR or UK? ').upper()
    country_list = [i[1] for i in country_link_list]
    if country not in country_list:
        print('Make sure you enter only the country letters, like US, CA, etc. ')
        adidas_country()
    return str(([i[0] for i in country_link_list if i[1] == country])[0])

link = adidas_country()
params = {
   'sz': 120,
   'grid': 'true',
   'start': 0
}

product_selector = '.image a'  
product_links = []  

captcha_class = '.g-recaptcha'  
site_key = 'data-sitekey'  



def new_session(url):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.36',
        'Accept': 'text/html, application/xhtml+xml, application/xml',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,da;q=0.6',
        'DNT': '1'
    })
    response = session.get(url, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup



def category_scraper(url, selector):
    category = new_session(url)
    for link_src in category.select(selector):
        product_links.append(link_src['href'])
    return product_links



def sitekey_scraper(url):
    product = new_session(url)
    selector_captcha = product.find_all(attrs={"class": "g-recaptcha"})
    if selector_captcha:
        captcha_attribute = selector_captcha[0]['data-sitekey']
        if captcha_attribute:
            print('\n\nSitekey Found on {}'.format(url))
            return captcha_attribute
    else:
        return


product_links = category_scraper(link, product_selector)


print("\nFound {} product links.".format(len(product_links)))
print("Starting site-key scraper. \n")
index = 0
for product in product_links:
    index += 1
    print('{} of {}: Checking for sitekey in: {}'.format(index, len(product_links), product))
    site_key_results = sitekey_scraper(str(product))
    if site_key_results:
        print("\Sitekey:\n\n{}\n".format(site_key_results))
        time.sleep(1)
        print("Copied to clipboard")
        pyperclip.copy(site_key_results)
        time.sleep(2)
        print(enjoyassci)
        time.sleep(4)
        break
    else:
        continue
