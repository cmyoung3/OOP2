class Phone:

    def main():

        def __init__(self,manufact,model,retail_price):
            self.__manufact = manufact
            self.__model = model
            self.__retail_price = retail_price

        def set_manufact(self, manufact):
            self.__manufact = manufact

        def set_model(self, model):
            self.__model = model

        def set_retail_price(self, retail_price):
            self.__retail_price = retail_price

        def get_manufact(manufact):
            print("Manufacturer:", manufact)

        def get_model(model):
            print("Model:", model)

        def get_retail_price(retail_price):
            print("Retail Price:", retail_price)

    main()
