import time

from appium.webdriver.common.appiumby import AppiumBy


class TestCartPage:
    def test_add_item_to_cart(self,driver):
        first_product=driver.find_element(AppiumBy.XPATH,'//androidx.recyclerview.widget.RecyclerView[@content-desc="Displays all products of catalog"]/android.view.ViewGroup[1]')
        first_product_name= driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Product Title" and @text="Sauce Labs Backpack"]').text
        first_product.click()
        time.sleep(2)
        add_cart_btn=driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cartBt")
        add_cart_btn.click()
        driver.back()
        second_product=driver.find_element(AppiumBy.XPATH,
                            '//androidx.recyclerview.widget.RecyclerView[@content-desc="Displays all products of catalog"]/android.view.ViewGroup[3]')
        second_product_name=driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Product Title" and @text="Sauce Labs Backpack (orange)"]').text
        second_product.click()
        time.sleep(2)
        add_cart_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
        add_cart_btn.click()
        driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cartIV").click()

        time.sleep(2)

        cart_items = driver.find_elements(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV")
        cart_item_names = [item.text for item in cart_items]

        assert first_product_name in cart_item_names, f"{first_product_name} sepette bulunamadı."
        assert second_product_name in cart_item_names, f"{second_product_name} sepette bulunamadı."








