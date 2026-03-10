from browser.driver_factory import create_driver
from monitors.newegg_monitor import NeweggMonitor
from utils.proxy_manager import get_proxy
from utils.data_formatter import create_dataframe


'''
    To Do:
        - Find a suitable time to query the page to avoid IP bans
        - Create Notification 
        - Route Notifications to Discord, Email, WhatsApp, or Text
        - add more bot commands
        - clean up discord message from bot to make more clean (text file maybe?)
        - add bestbuy
        - create option to 24/7 monitor
        - create README
        - redo commenting/notes
        

        Optional:
            - Create Bot to Auto Purchase based on Parameters


'''




def main():
  
    
    # Website we want to monitor
    url = "https://www.newegg.com/p/pl?N=100007709%2050001315%20601469157%20601469161"
    proxy = get_proxy()

    # Create Selenium driver using our factory
    driver = create_driver(headless=True, proxy=proxy)
    monitor = NeweggMonitor(url, driver)
    products = monitor.get_products()


    results = create_dataframe(products)

    # For Testing purposes
    print(results)


    # Close the browser when finished
    driver.quit()



if __name__ == "__main__":
    main()
    