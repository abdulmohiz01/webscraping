import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import ProxyType
from seleniumwire import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.by import By

proxy_list = [
    "104.239.105.125:6655:notutdrh:2gcfp2ryqjo9",
    "107.172.163.27:6543:notutdrh:2gcfp2ryqjo9",
    "136.0.207.84:6661:notutdrh:2gcfp2ryqjo9",
    "142.147.128.93:6593:notutdrh:2gcfp2ryqjo9",
    "198.23.239.134:6540:notutdrh:2gcfp2ryqjo9",
    "207.244.217.165:6712:notutdrh:2gcfp2ryqjo9",
    "216.10.27.159:6837:notutdrh:2gcfp2ryqjo9",
    "23.94.138.75:6349:notutdrh:2gcfp2ryqjo9",
    "64.64.118.149:6732:notutdrh:2gcfp2ryqjo9"
]

for proxy in proxy_list:
    proxy_host, proxy_port, proxy_user, proxy_pass = proxy.split(':')
    seleniumwire_options = {
        'proxy': {
            'http': f'http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
            'https': f'https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}',
            'no_proxy': 'localhost,127.0.0.1'
        }
    }
    chrome_options = Options()
    # chrome_options.proxy = Proxy({ 'proxyType': ProxyType.MANUAL, 'httpProxy': f'{proxy_host}:{proxy_port}' })
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(seleniumwire_options=seleniumwire_options, options=chrome_options)
    try:
        driver.get('https://httpbin.io/ip')
        ip_address = driver.find_element(By.TAG_NAME, 'body').text
        print(f'Proxy: {proxy_host}:{proxy_port} -> {ip_address}')
    except Exception as e:
        print(f'Proxy: {proxy_host}:{proxy_port} -> Error: {e}')
    finally:
        driver.quit()
