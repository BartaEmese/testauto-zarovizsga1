from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"

driver.get(URL)

email_test_value = ["teszt@elek.hu", "teszt@", ""]


def email_field(email1):
    email = driver.find_element_by_id("email")
    email.click()
    time.sleep(2)
    email.send_keys(email1)
    submit = driver.find_element_by_id("submit")
    submit.click()
    time.sleep(2)
    email.clear()


# TC1 helyesen kitöltött mező
email_field(email_test_value[0])
assert len(driver.find_elements_by_xpath('//div[@class="validation-error"]')) == 0

# TC2 helytelen kitöltött mező
email_field(email_test_value[1])
time.sleep(2)
assert driver.find_element_by_xpath(
    '//div[@class="validation-error"]').text == "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes."

# TC1 üres mező
email_field(email_test_value[2])
time.sleep(1)
assert driver.find_element_by_xpath('//div[@class="validation-error"]').text == "Kérjük, töltse ki ezt a mezőt."

driver.close()
