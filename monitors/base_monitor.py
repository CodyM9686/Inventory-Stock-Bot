'''
    Purpose: Creating the parent class, BaseMonitor to feed into other
             monitors such as BestBuy, NewEgg, etc.

'''

class BaseMonitor:

   #
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver

    # Creating get_product function
    def get_products(self):
        raise NotImplementedError("Subclasses must implement get_products()")