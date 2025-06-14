from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\ChromeDriver\chromedriver-win64\chromedriver.exe"
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/")
# Wait for a few seconds to see the result
eventsDictionary = {}
events = driver.find_elements(By.CSS_SELECTOR, "div.event-widget div.shrubbery ul.menu li ")
for idx, event in enumerate(events):
    eventsDictionary[idx] = {
        "time": event.find_element(By.CSS_SELECTOR, "time").text,
        "name": event.find_element(By.CSS_SELECTOR, "a").text,
    }
print(eventsDictionary)
# for event, details in eventsDictionary.items():
#     print(f"{details['time']} - {details['name']}")
time.sleep(5)
driver.close()  # Closes opened tab
driver.quit()  # Closes the browser and all its tabs
