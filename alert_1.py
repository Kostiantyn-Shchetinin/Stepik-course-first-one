from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_css_selector("button.btn.btn-primary")
button.click()
alert = browser.switch_to.alert
alert.accept()
value = int((browser.find_element_by_css_selector("span#input_value.nowrap").text))
fillin_text = calc(value)
field = browser.find_element_by_css_selector("input#answer.form-control")
field.send_keys(str(fillin_text))
button1 = browser.find_element_by_css_selector("div.container > button.btn.btn-primary")
button1.click()

time.sleep(10)

browser.quit()
