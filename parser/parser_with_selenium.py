import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome("./chromedriver")
browser.get("https://www.youtube.com/watch?v=mNJKCg4BjC8")
xpath = '//*[@id="count"]//*[@class="view-count style-scope ytd-video-view-count-renderer"]'
time.sleep(3)
wait = WebDriverWait(browser, 1000)


element = browser.find_element(by=By.XPATH, value=xpath)

print(element.text)

