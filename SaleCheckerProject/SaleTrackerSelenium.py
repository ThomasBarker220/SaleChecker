"""
@Today's Date : 2/27/2023

@Author : Thomas Barker
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from PIL import Image

if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
    }
    options = Options()
    options.add_argument('--headless')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36'
    options.add_argument('user-agent={0}'.format(user_agent))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
    driver.get("https://www.abercrombie.com/shop/us/p/textured-stitch-crew-sweater-51918825?seq=03&categoryId=86655&faceout=model")
    window_height = driver.execute_script(
        'return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );')
    driver.set_window_size(1920, window_height / 3)
    driver.implicitly_wait(5)
    item_name = driver.find_element(By.CSS_SELECTOR, 'h1')
    print(item_name.text)
    with open('ss.png', 'wb') as f:
        f.write(driver.get_screenshot_as_png())
    img = Image.open('ss.png')
    img.show()
    # image = driver.find_element(By.CLASS_NAME, "product-main-image")
    # src = image.get_attribute('src')
    # print(src)
    # response = requests.get(src, headers=header)
    # image_data = response.content
    # img = Image.open(BytesIO(image_data))
    # img.show()
    driver.quit()

