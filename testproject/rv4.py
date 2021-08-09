from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"

driver.get(URL)

input_field = driver.find_element_by_id("missingCity")
input_field.send_keys("")
button = driver.find_element_by_id("submit").click()
result = driver.find_element_by_id("result")

driver.close()
