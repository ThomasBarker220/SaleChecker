"""
@Today's Date : 2/27/2023

@Author : Thomas Barker
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
from PIL import Image
from io import BytesIO


if __name__ == '__main__':
    options = Options()
    # options.add_argument('--headless')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
    driver.get("https://www.abercrombie.com/shop/us/p/textured-stitch-crew-sweater-51918825?seq=03&categoryId=86655&faceout=model")
    driver.implicitly_wait(20)
    item_name = driver.find_element(By.CSS_SELECTOR, 'h1')
    print(item_name.text)
    image = driver.find_element(By.CSS_SELECTOR, "img")
    src = image.get_attribute('src')
    print(src)
    response = requests.get(src)
    img = Image.open(BytesIO(response.content))
    img.show()
    driver.quit()

