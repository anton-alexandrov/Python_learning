from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time



driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('file:///Users/antonaleksandrov/test_file.html')

time.sleep(1)

#find element by ID
by_id = driver.find_element_by_id('login')
print("ID:", by_id)

#find element by name
name = driver.find_element_by_name('username')
print('name:', name)

#find element by XPath
login_form_absolute = driver.find_element_by_xpath("/html/body/form[1]")
print('Absolute:', login_form_absolute)

login_form_relative = driver.find_element_by_xpath("//form[1]")
print('Relative:', login_form_relative)

login_form_id = driver.find_element_by_xpath("//form[@id='login']")
print('ID:', login_form_id)

#find element by class
content = driver.find_element_by_class_name('content')
print('Class name:', content)
driver.close()