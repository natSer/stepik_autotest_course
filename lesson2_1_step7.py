from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_css_selector("[id=treasure]")
x = x_element.get_attribute("valuex")
y = calc(x)

el=browser.find_element_by_css_selector("[id=answer]")
el.send_keys(y)
    
bt=browser.find_element_by_css_selector("[id=robotCheckbox]")
bt.click()

bt=browser.find_element_by_css_selector("[id=robotsRule]")
bt.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

