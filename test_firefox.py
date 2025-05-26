import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

SELENIUM_REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")

def test_example_com_firefox():
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_URL,
        options=options
    )
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
    driver.quit()
