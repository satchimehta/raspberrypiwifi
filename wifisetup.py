from selenium import WebDriver
from selenium.webdriver import FirefoxOptions
import time

javascript = “document.getElementById(\”checkbox\”).click();”
opts = FirefoxOptions()
opts.add_argument(“—headless”)

browser = WebDriver.Firefox(firefox_options=opts)
browser.get(“google.com”)
time.sleep(10)
print(browser.current_url)

login = browser.find_element_by_name("email")
login.send_keys("cubswifitesting@gmail.com")
browser.execute_script(javascript)
signInButton = browser.find_element_by_class_name("submit")
signInButton.click()

time.sleep(10)
browser.quit