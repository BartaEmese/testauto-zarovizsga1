from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"

driver.get(URL)

button_p = driver.find_element_by_id("submit")

coins = []
for coin in range(1, 101):
    button_p.click()
    result = driver.find_elements_by_id("//li")
    coins.append(coin)
    coin += 1

result = driver.find_elements_by_id("//li")

fej = []
iras = []
result_fej = "fej"
result_iras = "írás"
for i in coins:
    if coins.text == result_fej:
        fej.append(i)
    else:
        iras.append(i)

assert len(fej) >= 30

driver.close()
