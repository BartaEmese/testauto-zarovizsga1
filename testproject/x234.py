from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"

# Oldal betöltése
driver.get(URL)

a_test_value = ["99", "kiskutya", ""]
b_test_value = ["12", "12", ""]
result_value = ["222", "NaN", "NaN"]


def calculator(a, b):
    input_a = driver.find_element_by_id("a")
    input_a.send_keys(a)
    input_b = driver.find_element_by_id("b")
    input_b.send_keys(b)
    button = driver.find_element_by_id("submit")
    button.click()


# TC1 helyes kitöltés
calculator(a_test_value[0], b_test_value[0])
result = driver.find_element_by_id("result")
assert result.text == result_value[0]

# TC2 kitöltés nem számmal
driver.get(URL)
calculator(a_test_value[1], b_test_value[1])
result = driver.find_element_by_id("result")
assert result.text == result_value[1]

# TC3 kitöltés  üresen
driver.get(URL)
calculator(a_test_value[2], b_test_value[2])
result = driver.find_element_by_id("result")
assert result.text == result_value[2]


driver.quit()

