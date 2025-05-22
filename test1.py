from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def test_example_com_chrome():
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Assumes chromedriver is in PATH
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://example.com")
    assert "Example Domain" in driver.title
    driver.quit()

def test_example_com_firefox():
    options = FirefoxOptions()
    options.add_argument("--headless")

    # Assumes geckodriver is in PATH
    service = FirefoxService()
    driver = webdriver.Firefox(service=service, options=options)

    driver.get("https://example.com")
    assert "Example Domain" in driver.title
    driver.quit()
