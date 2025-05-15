import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from tests.utils import login, add_cart


class TestPaymentPage:

     @pytest.mark.parametrize("name,address,city,zipcode,country,error,expected_error_id", [
            ("seval", "Ankara", "AAnkara", "", "Türkiye", "Please provide your zip",
             "com.saucelabs.mydemoapp.android:id/zipErrorTV"),
            ("", "ankara", "AAnkara", "00", "Türkiye", "Please provide your full name.",
             "com.saucelabs.mydemoapp.android:id/fullNameErrorTV")
      ])
     def test_invalid_payment(self, driver, name, address, city, zipcode, country, error, expected_error_id):
         add_cart(driver)
         time.sleep(2)
         login(driver)
         time.sleep(2)
         name_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameET")
         name_input.send_keys(name)
         address_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ET")
         address_input.send_keys(address)
         city_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityET")
         city_input.send_keys(city)
         zipcode_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipET")
         zipcode_input.send_keys(zipcode)
         country_input = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryET")
         country_input.send_keys(country)
         payment_btn = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
         payment_btn.click()

         # Hata mesajı kontrolü
         error_text = driver.find_element(AppiumBy.ID, expected_error_id).text
         assert error_text == error

     def test_valid_payment(self, driver):
         # Ürün ekleme
         add_cart(driver)
         time.sleep(2)
         # Login
         login(driver)

         # Formu doldur
         driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameET").send_keys("Seval")
         driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ET").send_keys(
             "Atatürk Caddesi 123")
         driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityET").send_keys("Ankara")
         driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipET").send_keys("06000")
         driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryET").send_keys("Türkiye")

         # Ödeme yap
         driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn").click()
         time.sleep(2)
         # Başarılı mesaj kontrolü
         success_msg = driver.find_element(AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/enterPaymentMethodTV").text
         assert "Enter a payment method" in success_msg

         #kart bilgileri
         card_name=driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.saucelabs.mydemoapp.android:id/nameET"]')
         card_name.send_keys("Seval")
         card_number=driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/cardNumberET")
         card_number.send_keys("123456")
         date=driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/expirationDateET")
         date.send_keys("0606")
         code=driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/securityCodeET")
         code.send_keys("345")
         #review order
         driver.find_element(AppiumBy.ID,"com.saucelabs.mydemoapp.android:id/paymentBtn").click()




