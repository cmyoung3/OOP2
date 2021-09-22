class Car:
    
    #add year_model and make back to the __init__
    def __init__(self, model, brand):
            self.__year_model = model
            self.__make = brand
            self.__speed = 0

    #def Make_n_Model(self):
        #year_model = self.__make = input("What's the make of your car? ")
        #self.__year_model = input("What's the year and model of your car? ")
    def Model(self):
        self.__year_model
    
    def Make(self):
        self.__make

    def accelerate(self):
            self.__speed += 5
            

    def brake(self):
            self.__speed -= 5
           

    def get_speed(self):
        return self.__speed

    def get_Model(self):
        return self.__year_model

    def get_Make(self):
        return self.__make
        



            

        