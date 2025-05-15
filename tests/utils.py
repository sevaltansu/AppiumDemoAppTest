from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginTV").click()
    time.sleep(1)
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET").send_keys("bob@example.com")
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET").send_keys("10203040")
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn").click()
    time.sleep(2)
def add_cart(driver):
    first_product=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located( (AppiumBy.XPATH,
     '//androidx.recyclerview.widget.RecyclerView[@content-desc="Displays all products of catalog"]/android.view.ViewGroup[1]'))
    )
    first_product.click()
    add_cart_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
    add_cart_btn.click()
    time.sleep(2)
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV").click()
    time.sleep(2)
    driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt").click()