
from appium import webdriver
from appium.options.android import UiAutomator2Options
import pytest

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "11"
    options.device_name = "emulator-5554"
    options.app = "C:\\Users\\huawei\\Downloads\\mda-2.2.0-25.apk"
    options.automation_name = "UiAutomator2"
    options.auto_grant_permissions = True
    options.app_wait_activity = "*.*"


    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    yield driver
    #driver.quit()

