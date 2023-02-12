"""
@Today's Date : 2/8/2023

@Author : Thomas Barker
"""
import requests
from bs4 import BeautifulSoup
import re
import lxml
import pandas as pd


def check_sales(links):
    pricepattern = re.compile("(?i).*pric.*")
    pattern = "\d+"
    for link in links:
        r = requests.get(link, headers = header).content
        soup = BeautifulSoup(r, "lxml")
        curr_price_tag = soup.find_all('span', {"class" : pricepattern})
        price_list = []
        for price in curr_price_tag:
            list_price = price.text
            list_price = re.findall(pattern, list_price)
            price_list.append(int(list_price[0]))
        print("$" + str(min(price_list)))
        print(link)





if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
    }
    urls = ["https://bearbottomclothing.com/collections/shorts/products/loft"
            "-short",
            "https://www.patagonia.com/product/mens-hemp-work-sweatshirt"
            "/21399.html?cgid=mens-fleece",
            "https://www.abercrombie.com/shop/us/p/textured-stitch-crew"
            "-sweater-51918825?seq=03&categoryId=86655&faceout=model",
            "https://www.patagonia.com/product/mens-long-sleeved-cotton-in-conversion-lightweight-fjord-flannel-shirt/42410.html?dwvar_42410_color=BETB&cgid=web-specials-mens"]
    check_sales(urls)

# "https://oldnavy.gap.com/browse/product.do?pid=4743830120003&pcid=999&vid=1&searchText=waffle+knit#pdp-page-content"
