from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://www.python.org')
element_id = driver.find_element_by_id('id-search-field')
print(element_id)

element_name = driver.find_element_by_name("q")
print(element_name)

#heading_xpath = driver.find_element_by_xpath("//*[@id='mainContent']/h2[1]")
element_classname = driver.find_element_by_class_name('say-no-more')
print(element_classname)
driver.close()