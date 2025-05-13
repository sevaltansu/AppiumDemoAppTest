import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy



class TestLoginPage:
    def test_invalid_login(self, driver):
        driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/menuIV").click()
        time.sleep(2)
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Login Menu Item"]').click()
        username_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
        username_input.send_keys("")
        password_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
        password_input.send_keys("")
        lgn_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")
        lgn_btn.click()
        error_msg = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameErrorTV")
        error_msg_text = error_msg.text
        assert error_msg_text == "Username is required"

    def test_valid_login(self,driver):
        driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/menuIV").click()
        time.sleep(2)
        driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Login Menu Item"]').click()
        username_input=driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/nameET")
        username_input.send_keys("bod@example.com")
        password_input=driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/passwordET")
        password_input.send_keys("10203040")
        lgn_btn=driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/loginBtn")
        lgn_btn.click()
        time.sleep(5)







