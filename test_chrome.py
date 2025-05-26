import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

SELENIUM_REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL", "http://localhost:4444/wd/hub")

def test_example_com_chrome():
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Remote(
        command_executor=SELENIUM_REMOTE_URL,
        options=options
    )
    driver.get("https://example.com")
    assert "Example Domain" in driver.title
    driver.quit()
