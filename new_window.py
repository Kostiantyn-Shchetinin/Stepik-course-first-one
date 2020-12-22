from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
button.click()
second_window = browser.window_handles[1]
first_window = browser.window_handles[0]
browser.switch_to.window(second_window)
value = int((browser.find_element_by_css_selector("span#input_value.nowrap").text))
fillin = calc(value)
field = browser.find_element_by_css_selector("input#answer.form-control")
field.send_keys(fillin)
button1 = browser.find_element_by_css_selector("div.container > button.btn.btn-primary")
button1.click()

time.sleep(10)
browser.quit()
