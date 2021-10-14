import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_webdriver():
    chrome_driver = str(os.environ.get("CHROME_DRIVER"))
    if chrome_driver is None:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        return webdriver.Chrome(options=chrome_options)

    return webdriver.Chrome(chrome_driver)
