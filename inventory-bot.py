from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from tabulate import tabulate
import time
import pandas as pd


'''
To Do:

    - Create Bot Functionality
        - Create Selium connection - DONE
        - Get List
        - Return List Using Panda
        - Find a suitable time to query the page to avoid IP bans
        - Connect Data to discord Bot
    
Optional:
    - Create Bot to Auto Purchase based on Parameters
'''

class InventoryBot():
    def __init__(self):
        self.stock_data = []
        
    def scraped_data(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging']) # research into before running officially
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.newegg.com/p/pl?N=100007709%2050001315%20601469157%20601469161")
       # driver.get("https://www.newegg.com/p/pl?N=50001315%20601469155%20100007709&d=9070+xt+graphics+card")
       # driver.get("https://www.newegg.com/p/pl?d=gpu&N=601469157%20601469160%20601469158%20100007709") # Testing available/multiple listings
        

        #try: -> add while statement for turning on and off
        # add random times to avoid bot detection
        products = driver.find_elements(By.CLASS_NAME, "item-container") 
       # try:
        for product in products:
            try:
                promo_element = product.find_element(By.CLASS_NAME, "item-promo")
                if promo_element.text.strip() == 'OUT OF STOCK':
                    continue
            except NoSuchElementException:
                pass
                
                item_stock = 'IN STOCK'
                item_title = product.find_element(By.CLASS_NAME, "item-title")
                item_price = product.find_element(By.CLASS_NAME, "price-current")
                item_info = product.find_element(By.CLASS_NAME, "item-info") # not in use right now
                item_link = item_title.get_attribute('href')
                product_title = item_title.text.strip()
                if '12GB' in product_title:
                    product_title = product_title.split('12GB', 1)[0] + '12GB'
                elif '16GB' in product_title:
                    product_title = product_title.split('16GB', 1)[0] + '16GB' # If I make it for multiple items, I will need to add condition
                elif '32GB' in product_title:
                    product_title = product_title.split('32GB', 1)[0] + '32GB'
                if type(item_stock) != str:
                    item_stock = item_stock.text.strip()
                
                item_price = item_price.text.strip().split('$', 1)[1]
                #print(product_title + " - " + item_stock + " - Price: $"+ item_price + " - " + item_link)
                self.stock_data.append({
                    'Product': product_title,
                    'Availability': item_stock,
                    'Price': '$'+item_price,
                    'Link': item_link
                    })
            except Exception as e:
                print(f"Error occured while processing a product: {e}")
                
        #except:
           # print("An Error occured.")
        
        driver.quit() 
        if not self.stock_data:
            response = "No items are in-stock. I'll keep looking though :/"
            return response
            
        
        return self.stock_data
    def create_dataframe(self):
        stock_data = self.scraped_data()
        if type(stock_data) == str:
            print(stock_data)
        else:
        #stock_data = [
       #     {'Product': 'ASUS TUF Gaming GeForce RTX 5070 Ti OC Edition 16GB', 'Availability': 'OUT OF STOCK', 'Price': '$999.99', 'Link': 'https://www.newegg.com/asus-tuf-gaming-tuf-rtx5070ti-o16g-gaming-nvidia-geforce-rtx-5070-ti-16gb-gddr7/p/N82E16814126754'},
        #    {'Product': 'ASUS PRIME GeForce RTX 5070 Ti 16GB', 'Availability': 'OUT OF STOCK', 'Price': '$939.99', 'Link': 'https://www.newegg.com/asus-prime-rtx5070ti-o16g-nvidia-geforce-rtx-5070-ti-16gb-gddr7/p/N82E16814126756'},
       #     {'Product': 'ASUS PRIME GeForce RTX 5070 Ti 16GB', 'Availability': 'OUT OF STOCK', 'Price': '$749.99', 'Link': 'https://www.newegg.com/asus-prime-rtx5070ti-16g-nvidia-geforce-rtx-5070-ti-16gb-gddr7/p/N82E16814126757'}
       #     ]
        
            df = pd.DataFrame(stock_data)
        
            #print(df) # make look pretty

            table = tabulate(df, headers='keys',tablefmt='grid',showindex=False)

            print(table)


    def testing(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging']) # research into before running officially
        driver = webdriver.Chrome(options=options)
       # driver.get("https://www.newegg.com/p/pl?N=100007709%2050001315%20601469157%20601469161")
        #driver.get("https://www.newegg.com/p/pl?N=50001315%20601469155%20100007709&d=9070+xt+graphics+card")
        driver.get("https://www.newegg.com/p/pl?d=gpu&N=601469157%20601469160%20601469158%20100007709") # Testing available/multiple listings
        

        #try: -> add while statement for turning on and off
        # add random times to avoid bot detection
        products = driver.find_elements(By.CLASS_NAME, "item-container") 
       # try:
        for product in products:
            
            try:
                item_stock = product.find_element(By.CLASS_NAME, "item-promo")
            except:
                print("No promo code found. Is it in stock?")
                item_stock = ''
            item_title = product.find_element(By.CLASS_NAME, "item-title")
            
            item_price = product.find_element(By.CLASS_NAME, "price-current")
            item_info = product.find_element(By.CLASS_NAME, "item-info") # not in use right now
            item_link = item_title.get_attribute('href')

            product_title = item_title.text.strip().split('16GB', 1)[0] + '16GB' # If I make it for multiple items, I will need to add condition
            if type(item_stock) is str:
                item_stock
            else:
                item_stock = item_stock.text.strip()
            item_price = item_price.text.strip().split('$', 1)[1]
            #print(product_title + " - " + item_stock + " - Price: $"+ item_price + " - " + item_link)
            self.stock_data.append({
                'Product': product_title,
                'Availability': item_stock,
                'Price': '$'+item_price,
                'Link': item_link
                })
            
        #except:
           # print("An Error occured.")
        
        driver.quit() 
        return self.stock_data

if __name__ == "__main__":
    inv = InventoryBot()
    start_time = time.time()
    inv.create_dataframe()
    print("--- %s seconds ---" % (time.time() - start_time))