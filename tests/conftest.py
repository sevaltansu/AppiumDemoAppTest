
from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest

@pytest.fixture(scope="module")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "14"  # Android sürümü
    options.device_name = "emulator-5554"  # Emulator cihaz adı
    options.app = "C:\\Users\\huawei\\Downloads\\mda-2.2.0-25.apk"  # APK dosyasının yolu
    options.automation_name = "UiAutomator2"

    # Appium server'a bağlanmak için WebDriver'ı başlatıyoruz
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    yield driver

