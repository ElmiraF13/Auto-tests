import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])

class TestLogin:
    def test_login_on_stepic(self, browser, lesson):
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.implicitly_wait(5)
        browser.get(link)
        browser.find_element(By.ID, "ember33").click()
        input1 = browser.find_element(By.NAME, "login").send_keys("ЛОГИН")
        input1 = browser.find_element(By.NAME, "password").send_keys("ПАРОЛЬ")
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader").click()
        browser.find_element(By.CSS_SELECTOR, ".top-tools__lesson-name")