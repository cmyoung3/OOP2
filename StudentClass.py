from datetime import date

class Student:
#self represents the whole object
    def __init__(self, id, name, dob, classification):
        self.__stendentid = id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
        self.__age = 0
        self.__register = ''

    def get_age(self):
        return self.__age
    
    def get_registration(self):
        return self.__register

    def register(self):
        #classification = input("What's your classification? ")
        if self.__classification == 'Freshmen':
            self.__register = '11/10 thru 11/12'

        elif self.__classification == 'Sophomores':
            self.__register = '11/7 thru 11/9'
        
        elif self.__classification == 'Juniors':
            self.__register = '11/4 thru 11/6'

        elif self.__classification == 'Senior':
            self.__register = '11/1 thru 11/3'

        else:
            self.__register = 'classification not found'

    def calc_age(self):
        bday = self.__dob.split('/')
        t = date.today()
        print(t.year)
        bday_year = int(bday[2])
        self.__age = t.year - bday_year


    

