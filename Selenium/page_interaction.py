from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://python.org")

search = driver.find_element_by_name('q')
search.clear()
search.send_keys('pycon')
search.send_keys(Keys.RETURN)
time.sleep(4)

driver.close()

driver2 = webdriver.Chrome(ChromeDriverManager().install())
driver2.get('file:///Users/antonaleksandrov/test_file.html')
select_elem = Select(driver2.find_element_by_name('numReturnSelect'))
select_elem.select_by_index(2)
time.sleep(2)

select_elem.select_by_visible_text('200')
time.sleep(2)

select_elem.select_by_value('250')
time.sleep(2)

option = select_elem.options
print(option)

submit_button = driver2.find_element_by_name('continue_select')
submit_button.submit()
time.sleep(2)

driver2.close()