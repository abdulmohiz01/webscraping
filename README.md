# Webscraping & Automation

This repository contains two main Python web automation/scraping projects:

<a style='font-size:26px' href='https://orteil.dashnet.org/experiments/cookie/'>1. Cookie Hunter</a>
----------------

- Automates playing the Cookie Clicker game by auto-clicking on the main cookie.
- Uses Selenium with chrome driver to interact with the game in a browser.
- Continuously clicks the cookie to increase the score automatically.
- May include logic for purchasing upgrades or handling game events.
<img src="cookie_hunter.png" />

<a style='font-size:26px' href='https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.66992536176795%2C%22north%22%3A37.88050759203448%7D%2C%22mapZoom%22%3A12%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%7D' >2. Zillow Rental Research</a>
-------------------------

- Scrapes rental property data from Zillow for a specified location (San Francisco, CA).
- Uses Selenium (with undetected_chromedriver) to load the Zillow rentals page.
- Extracts property cards, collecting address, price, and listing link for each property in bulk.
- Automates filling a Google Form with the scraped property data:
    - For each property, enters address, price, and link into the form.
    - Submits the form and reloads for the next entry.
    - Handles dynamic page elements and possible exceptions (e.g., stale elements, missing links).
- Includes error handling and waits to ensure reliable automation.

<img src="zillow_sheet.png" />

- Both projects are written in Python and use Selenium for browser automation.
- This repository is intended for educational purposes only. I mean no harm to anyone, and all scripts are for learning and demonstration.