import time
from appium.webdriver.common.appiumby import AppiumBy
from tests.utils import login


class TestPaymentPage:
    def test_payment_page(self,driver):
        first_product = driver.find_element(AppiumBy.XPATH,
                                            '//androidx.recyclerview.widget.RecyclerView[@content-desc="Displays all products of catalog"]/android.view.ViewGroup[1]')
        first_product.click()
        add_cart_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
        add_cart_btn.click()
        time.sleep(2)
        driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cartIV").click()
        time.sleep(2)
        driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cartBt").click()
        #giriş yap
        login(driver)
        time.sleep(2)
        fields = {
            "Full Name": "com.saucelabs.mydemoapp.android:id/fullNameET",
            "Address Line": "com.saucelabs.mydemoapp.android:id/address1ET",
            "City": "com.saucelabs.mydemoapp.android:id/cityET",
            "Zip Code": "com.saucelabs.mydemoapp.android:id/zipET",
            "Country": "com.saucelabs.mydemoapp.android:id/countryET"
        }

        filled_data = {
            "Full Name": "Seval Tansu",
            "Address Line": "Yıldız Mah.",
            "City": "İstanbul",
            "Zip Code": "34000",
            "Country": "Turkey"
        }
        for field, element_id in fields.items():
            input_element = driver.find_element(AppiumBy.ID, element_id)
            input_element.send_keys(filled_data[field])
            time.sleep(0.5)
        continue_button = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
        continue_button.click()
        time.sleep(2)