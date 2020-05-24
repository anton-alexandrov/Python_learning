from selenium import webdriver
#You can automatically use the correct chromedriver by using the webdrive-manager.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

#if driver is not in PATH
#driverLocation = "/Users/antonaleksandrov/My Documents/Coding/Selenium/Drivers/chromedriver"
#browser = webdriver.Chrome(driverLocation)

#for Chrome
browser1 = webdriver.Chrome(ChromeDriverManager().install())
browser1.get('http://www.seleniumhq.org')
browser1.close()

#for Safari
browser = webdriver.Safari()
browser.get('http://www.python.org')
elem = browser.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(8)
browser.close()


