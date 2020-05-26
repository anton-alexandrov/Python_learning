from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://wiki.python.org/moin/FrontPage")
search_element = driver.find_element_by_id("searchinput")
search_element.clear()
search_element.send_keys('Beginner')
search_element.send_keys(Keys.RETURN)


select=Select(driver.find_element_by_xpath("/html/body/div[2]/div[3]/ul/li[5]/form/div/select"))
print(select)
select.select_by_visible_text('Raw Text')
time.sleep(2)



driver.close()
