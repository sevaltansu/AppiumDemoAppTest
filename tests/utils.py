from appium.webdriver.common.appiumby import AppiumBy
import time

def login(driver):
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginTV").click()
    time.sleep(1)
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET").send_keys("bob@example.com")
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET").send_keys("10203040")
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn").click()
    time.sleep(2)
