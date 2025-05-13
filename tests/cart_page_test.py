import time

from appium.webdriver.common.appiumby import AppiumBy


class TestCartPage:
    def test_add_item_to_cart(self,driver):
        driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@content-desc="Displays all products of catalog"]/android.view.ViewGroup[1]').click()
        time.sleep(2)
        add_cart_btn=driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cartBt")
        add_cart_btn.click()
        driver.back()
        driver.find_element(AppiumBy.XPATH,
                            '//androidx.recyclerview.widget.RecyclerView[@content-desc="Displays all products of catalog"]/android.view.ViewGroup[3]').click()
        time.sleep(2)
        add_cart_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
        add_cart_btn.click()


