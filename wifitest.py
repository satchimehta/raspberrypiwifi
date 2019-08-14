from selenium import webdriver
import time
try:
    browser = webdriver.Firefox()
    url = browser.get('https://www.google.com')
    
    while((browser.current_url!= "https://www.google.com/") and (browser.current_url!= "https://www.wifiatwrigley.com/connected")):
        print(browser.current_url)
        time.sleep(1)
    
    browser.quit()
    
except:
    print("ERROR- WIFI DISCONNECTED")