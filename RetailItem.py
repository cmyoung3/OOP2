class RetailItem:

    def __init__(self, desc, inv, price):
            self.__desc = desc
            self.__inv = inv
            self.__price = price
        

    def get_Description(self):
        return self.__desc
    
    def get_Inventory(self):
        return self.__inv

    def get_Price(self):
        return self.__price
    


    #add inv and price later
    