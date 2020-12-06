from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector(".card-body > button#book")

t = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), "$100")
)
print(t)
print(button)
button.click()
browser.execute_script("window.scrollBy(0, 400);")
x = int(browser.find_element_by_css_selector("span.nowrap#input_value").text)
fill_in = calc(x)
field = browser.find_element_by_css_selector("input.form-control#answer")
field.send_keys(str(fill_in))
button_f = browser.find_element_by_css_selector("button#solve")

button_f.click()
time.sleep(10)

browser.quit()




