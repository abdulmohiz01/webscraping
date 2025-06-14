import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.support.wait import WebDriverWait

options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36")

driver = uc.Chrome(options=options)
driver.get(
    "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-122.60935268072842%2C%22east%22%3A-122.20766505865811%2C%22south%22%3A37.63681178454677%2C%22north%22%3A37.84748816484141%7D%2C%22mapZoom%22%3A12%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%7D")
time.sleep(15)

houses = {}
house_id = 0
page = 2
while True:

    element = driver.find_element(By.CSS_SELECTOR, "div.search-pagination")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(3)

    property_cards = driver.find_elements(By.CSS_SELECTOR, 'article[data-test="property-card"]')

    for card in property_cards:
        try:
            link_elem = card.find_element(By.CSS_SELECTOR, 'div#swipeable div a')
            price_elem = card.find_element(By.CSS_SELECTOR, "span[data-test='property-card-price']")
            try:
                address_elem = card.find_element(By.TAG_NAME, "address")
                address = address_elem.text
            except Exception:
                address = "Address not available"
            houses[house_id] = {
                "link": link_elem.get_attribute("href"),
                "price": price_elem.text,
                "address": address
            }
            house_id += 1

        except Exception as e:
            print("Error", e)

    print(f"Page {page - 1} processed.")
    print("Gathered houses:", len(houses))

    try:
        next_button = driver.find_element(By.LINK_TEXT, f"{page}")
        next_button.click()
        print(f"Navigated to page {page}")
        page += 1
        time.sleep(random.randrange(5, 10))
    except Exception:
        print("No more pages.")
        break

for key, value in houses.items():
    print(f"{key}: {value['address']} - {value['price']} - {value['link']}")

print('Filling form')
driver.get(
    "https://docs.google.com/forms/d/e/1FAIpQLSdDhW48X1c-HdmqPNGo4d4oyiDZSyF7JV9UVuw1x8jWiouQsw/viewform?usp=dialog")

for key, value in houses.items():
    wait = WebDriverWait(driver, 15)
    address_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby='i1 i4']")))
    price_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby='i6 i9']")))
    link_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-labelledby='i11 i14']")))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']")))
    address_input.click()
    address_input.send_keys(value['address'])
    price_input.click()
    price_input.send_keys(value['price'])
    link_input.click()
    link_input.send_keys(value['link'])
    button.click()
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSdDhW48X1c-HdmqPNGo4d4oyiDZSyF7JV9UVuw1x8jWiouQsw/viewform?usp=dialog")
    time.sleep(4)

print("Form filled for all properties.")

driver.close()
