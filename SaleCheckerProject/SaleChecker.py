"""
@Today's Date : 2/8/2023

@Author : Thomas Barker
"""
import requests
from bs4 import BeautifulSoup
import re
import lxml
import pandas as pd


def check_sales(links, df):
    pricepattern = re.compile("(?i).*pric.*")
    pattern = "\d+"
    if len(df.iloc[0]) != 0:
        currentpricelist = df.iloc[0,:].astype(int).tolist()
        print(currentpricelist)
    newitemlist = []
    newpricelist = []
    reduced_prices = []

    for index, link in enumerate(links):

        r = requests.get(link, headers = header).content
        soup = BeautifulSoup(r, "lxml")

        curr_price_tag = soup.find_all('span', {"class" : pricepattern})
        if curr_price_tag == None:
            curr_price_tag = soup.find_all('div', {"class" : pricepattern})

        item_name_tag = soup.find('h1')
        if item_name_tag != None:
            item_name = item_name_tag.text
            item = item_name.strip()
            newitemlist.append(item)
            print(item)

        price_list = []
        for price in curr_price_tag:
            list_price = price.text
            list_price = re.findall(pattern, list_price)
            if len(list_price) > 0:
                price_list.append(int(list_price[0]))
        updated_price = min(price_list)

        if item in df.columns:
            if updated_price < int(df[item]):
                reduced_prices.append((item, updated_price, link))

        df[item] = updated_price
        newpricelist.append("$" + str(updated_price))
        print("$" + str(min(price_list)))
        print(link)
    df = df[newitemlist]
    print(reduced_prices)










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
            "https://www.patagonia.com/product/mens-long-sleeved-cotton-in"
            "-conversion-lightweight-fjord-flannel-shirt/42410.html?dwvar_42410_color=BETB&cgid=web-specials-mens",
            "https://unitedbyblue.com/products/mens-indigo-throwback"
            "-sweatshirt",
            "https://bananarepublicfactory.gapfactory.com/browse/product.do"
            "?pid=580739001&cid=1045334&pcid=1045334&vid=1&nav=meganav%3AMen%3AMen%27s+Clothing%3ASweaters&cpos=18&cexp=368&kcid=CategoryIDs%3D1045334&cvar=2363&ctype=Listing&cpid=res23021722208407532520781#pdp-page-content"]

    df = pd.read_csv(r'C:\Users\tbark\PycharmProjects\SaleChecker'
                     r'\SaleCheckerProject\SaleTrackerSheet.csv')

    check_sales(urls, df)

    df.to_csv(r'C:\Users\tbark\PycharmProjects\SaleChecker\SaleCheckerProject'
              r'\SaleTrackerSheet.csv', index=False)

#"https://www.pacsun.com/polo-ralph-lauren/rainbow-logo-crew-neck-sweatshirt-0190600100057.html?tileCgid=mens"