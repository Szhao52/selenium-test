import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

SELENIUM_REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")

def test_example_com_chrome():
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_URL,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
    driver.quit()

def test_example_com_firefox():
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_URL,
        desired_capabilities=DesiredCapabilities.FIREFOX
    )
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
    driver.quit()
