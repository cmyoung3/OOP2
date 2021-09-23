class Car:
    
    
    def __init__(self, year_model, make):
            self.__year_model = year_model
            self.__make = make
            self.__speed = 0

    
    def Model(self):
        self.__year_model
    
    def Make(self):
        self.__make

    def get_Model(self):
        return self.__year_model
    
    def get_Make(self):
        return self.__make

    def accelerate(self):
            self.__speed += 5        

    def brake(self):
            self.__speed -= 5
           

    def get_speed(self):
        return self.__speed


        



            

        