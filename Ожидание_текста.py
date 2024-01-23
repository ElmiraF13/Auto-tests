from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд) .text_to_be_present_in_element((By.ID, "здесь пишем ID"), "здесь текст")
text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element(By.ID, "book")
button.click()

import math
	
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
	  
x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
x = x_element.text
y = calc(x)
    
x_element = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
x_element.send_keys(y)
button = browser.find_element(By.ID, "solve")
button.click()
    
time.sleep(7)
browser.quit()