from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)
field1 = browser.find_element_by_css_selector("[name = "firstname"]")
field2 = browser.find_element_by_css_selector("[name = "lastname"]")
field3 = browser.find_element_by_css_selector("[name = "email"]")
field1.send_keys("Kostiantyn")
field2.send_keys("Shchetinin")
field3.send_keys("k-shchetinin@ukr.net")

current_dir = os.path.abspath(os.path.dirname(__file__))

file_name = "test_file.txt"

file_path = os.path.join(current_dir, file_name)

add_file = browser.find_element_by_css_selector("input#file")

add_file.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn.btn-primary")

buton.click()

time.sleep(10)
browser.quit()


