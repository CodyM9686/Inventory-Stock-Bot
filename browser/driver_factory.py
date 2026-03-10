from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
    Purpose:
    Creating Driver Function to create driver and apply options as needed

    TO-DO: 
    - Research more options to ensure compatiability on all platforms
    - Remove headless parameter option in future development to force headless mode.

'''
def create_driver(headless=True, proxy=None):
    
    options = Options()

    if headless:
        options.add_argument("--headless")
    
    if proxy:
        options.add_argument(f'--proxy-server={proxy}')

    driver = webdriver.Chrome(options=options)
    return driver

