import time

from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\ChromeDriver\chromedriver-win64\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Main_Page")
count = driver.find_element(By.ID, "articlecount").find_element(By.TAG_NAME, "a")
getlink = driver.find_element(By.LINK_TEXT, "encyclopedia")
# getlink.click()

icon= driver.find_element(By.CSS_SELECTOR, "span.mw-ui-icon-search")
search = driver.find_element(By.NAME, "search")
icon.click()
search.send_keys("Dickies")
search.send_keys(Keys.RETURN)




time.sleep(25)
print(count.text)