from monitors.base_monitor import BaseMonitor
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

'''
    Purpose:
    Create the primary NewEggMonitor that web scrapes data from the NewEgg website.

    TO-DO: 
    - Optimization of scraping performance to reduce page load time and improve data extraction efficiency.

'''


# NeweggMonitor inherits from BaseMonitor
class NeweggMonitor(BaseMonitor):
    ''' 
        Hardcoding URL and Driver for time being until future implementation can 
        resolve this through adding user functionality to include their own URL.

    '''
    def __init__(self, url=None, driver=None):
        url = url or 'https://www.newegg.com/p/pl?N=100007709%2050001315%20601469157%20601469161'
        from browser.driver_factory import create_driver
        driver = driver or create_driver(headless=True)
        super().__init__(url, driver)

    def get_products(self):
        self.driver.get(self.url)

        # Initilize stock_data
        self.stock_data = [] 

        products = self.driver.find_elements(By.CLASS_NAME, "item-container")

        for product in products:

            try:
                promo_element = product.find_element(By.CLASS_NAME, "item-promo")
                if promo_element.text.strip() == 'OUT OF STOCK':
                    continue

            # If the promo element doesn't exist we ignore the error
            except NoSuchElementException:
                pass

                # If we reach this point the item is considered in stock
                item_stock = 'IN STOCK'
                # Find product title element
                item_title = product.find_element(By.CLASS_NAME, "item-title")

                # Find price element
                item_price = product.find_element(By.CLASS_NAME, "price-current")

                # Will be used for future development
                item_info = product.find_element(By.CLASS_NAME, "item-info")
                
                item_link = item_title.get_attribute('href')
                product_title = item_title.text.strip()


                # Clean product title so it ends at VRAM size
                if '12GB' in product_title:
                    product_title = product_title.split('12GB', 1)[0] + '12GB'

                elif '16GB' in product_title:
                    product_title = product_title.split('16GB', 1)[0] + '16GB'

                elif '32GB' in product_title:
                    product_title = product_title.split('32GB', 1)[0] + '32GB'

                # Ensure item_stock is a string
                if type(item_stock) != str:
                    item_stock = item_stock.text.strip()


                # Extract price text and remove extra characters
                item_price = item_price.text.strip().split('$', 1)[1]


                # Store product data in dictionary
                self.stock_data.append({

                    'Product': product_title,
                    'Availability': item_stock,
                    'Price': '$' + item_price,
                    'Link': item_link

                })

            # Catch errors for individual products so the scraper keeps running
            except Exception as e:
                print(f"Error occurred while processing a product: {e}")

         # If no products were found in stock
        if not self.stock_data:

            response = "No items are in-stock. :/"

            return response

        return self.stock_data