from selenium import webdriver

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=webdriver.ChromeOptions()
)

driver.get('https://www.google.com')
print(driver.title)
driver.quit()