from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = r"C:\ChromeDriver\chromedriver-win64\chromedriver.exe"
driver= webdriver.Chrome(service=Service(executable_path=chrome_driver_path))
driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Sky")
last_name= driver.find_element(By.NAME, "lName")
last_name.send_keys("Lark")
email = driver.find_element(By.NAME, "email")
email.send_keys("123@gmail.com")
driver.find_element(By.CSS_SELECTOR, "button.btn").click()


time.sleep(15)

