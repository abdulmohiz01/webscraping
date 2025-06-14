from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = r"C:\ChromeDriver\chromedriver-win64\chromedriver.exe"
driver = webdriver.Chrome(service=Service(executable_path=chrome_driver_path))
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
while True:
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    cookie.click()
    # time.sleep(0.1)  # Click every 100 milliseconds

    # Check if the game is over
    # try:
    #     driver.find_element(By.ID, "gameOver")
    #     print("Game Over!")
    #     break
    # except:
    #     pass
