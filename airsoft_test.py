from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "https://stage.airsofter.world/ua/signup"

browser = webdriver.Chrome()
browser.get(link)
browser.execute_script("window.scrollBy(0, 300);")
f_username = browser.find_element_by_css_selector("#signupform-username")
f_username.send_keys("Toad1")
time.sleep(3)
f_email = browser.find_element_by_css_selector("#signupform-email")
f_email.send_keys("k-shchetiniin@ukr.net")
time.sleep(3)
browser.execute_script("window.scrollBy(0, 100);")
f_password = browser.find_element_by_css_selector("#signupform-password")
f_password.send_keys("123456")
select1 = browser.find_element_by_css_selector("#select2-signupform-region_id-container")

#select1.select_by_visible_text("Запорізька область")
select1.click()
browser.execute_script("window.scrollBy(0, 100);")
time.sleep(3)
choose_reg_vi = browser.find_element_by_css_selector("#select2-signupform-region_id-result-lkop-2")
choose_reg_vi.click()
select2 = browser.find_element_by_css_selector("#select2-signupform-city_id-container")
#select2.click()
#choose_zp = browser.find_element_by_css_selector("#select2-signupform-city_id-result-5woy-742")
#choose_zp.click()
time.sleep(3)
checkbox = browser.find_element_by_css_selector("div.checkbox > label")
checkbox.click()
button = browser.find_element_by_css_selector("button.submit-button")
button.click()
browser.quit()


