import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])

class TestLogin:
    def test_login_on_stepic(self, browser, lesson):
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.implicitly_wait(15)
        browser.get(link)
        browser.find_element(By.ID, "ember33").click()
        input1 = browser.find_element(By.NAME, "login").send_keys("ЛОГИН")
        input2 = browser.find_element(By.NAME, "password").send_keys("ПАРОЛЬ")
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader").click()
        browser.find_element(By.CSS_SELECTOR, ".top-tools__lesson-name")
        
        import math
        
        time.sleep(3)
        
        answer = math.log(int(time.time()))
        input3 = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
        is_disabled = input3.get_attribute('disabled')
        if is_disabled:
            button1 = WebDriverWait(browser, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".again-btn"))
                )
            button1.click()
        time.sleep(5)
        input3 = browser.find_element(By.CSS_SELECTOR, ".ember-text-area").send_keys(answer)
        
        button2 = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
            )
        button2.click()
        time.sleep(5)
        message = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
            )
        
        assert message.text == "Correct!", "Text must be 'Correct!'"