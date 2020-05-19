from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

driverPath = "C://Users//Sam//Documents//chromedriver.exe"

driver = webdriver.Chrome(driverPath)
driver.maximize_window()
driver.get("https://drizly.com/beer/ale/ipa/c15")
assert "Drizly" in driver.title

f = open("beer.txt", "w")
delay = 20

try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'CatalogItemCard__ProductName___4KWmV')))
    print("Page is ready!")
except (TimeoutException):
    print("ur internet ass")

time.sleep(10)
driver.find_element_by_class_name("CatalogItemCard__ProductName___4KWmV").click()

# for element in range(len(elements)):
#     info = {"Name": "", "ABV": "", "Category": "", "IBU": "", "brewer": "", "Region": "", "Calories": "", "Carbs": ""}
#     driver.find_element_by_xpath("//div[@class='CatalogGrid__CatalogListItem___3S6W5'][" + str(element) + "]//p[@class='CatalogItemCard__ProductName___4KWmV']").click()
#     myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'PDPAttributesAndReviews__row___3T_tv')))
#     rows = driver.find_elements_by_class_name("PDPAttributesAndReviews__row___3T_tv")
    # for row in range(len(rows)):
    #     x = driver.find_element_by_xpath("//dd[@class='PDPAttributesAndReviews__row___3T_tv'][" + str(row) + "]//dt[@class='PDPAttributesAndReviews__row__label___3DksY']")
    #     if x.text in info:
    #         info[x.text.strip()] = driver.find_element_by_xpath("//dd[@class='PDPAttributesAndReviews__row___3T_tv'][" + row + "]//dd[@class='PDPAttributesAndReviews__row__value___1EoK']").text
    #     else:
    #         continue
    #f.write(info)
    #driver.back()

f.close()            