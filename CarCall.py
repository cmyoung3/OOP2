import CarType as c
year_model = '2008'
make = 'Mazda'

a = c.Car(year_model,make)
a.get_Make
a.get_Model

for x in range(5):
    a.accelerate()
    print('-- Your current speed is', a.get_speed())

for x in range(5):
    a.brake()
    print('-- Your current speed is', a.get_speed())
    
    







