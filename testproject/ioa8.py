from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"

driver.get(URL)

num1_l = []
op_l = []
num2_l = []
result_l = []

num1 = driver.find_element_by_id("num1")
num1_l.append(num1.text)
op = driver.find_element_by_id("op")
op_l.append(op.text)
num2 = driver.find_element_by_id("num2")
num2_l.append(num2.text)
button = driver.find_element_by_id("submit")
button.click()
time.sleep(2)
result = driver.find_element_by_xpath("/html/body/div/div/span")
result_l.append(result.text)



# driver.close()
