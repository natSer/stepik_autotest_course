
from selenium import webdriver
import time
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element as tbe
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(tbe((By.ID, "price"), "10000 RUR"))
browser.find_element_by_id("book").click()

x=int(browser.find_element_by_id("input_value").text)
y=math.log(abs(12.*math.sin(x)))

browser.find_element_by_id("answer").send_keys(str(y))
browser.find_element_by_id("solve").click()



