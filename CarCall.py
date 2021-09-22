import CarType as c

model = "2008 Mazda3"
brand = "Mazda"

#car = c.Car(m,b)
a = c.Car(model, brand)

#print(m,b)
print(a.get_Model, a.get_Make)
for x in range(5):
    a.accelerate()
    print('-- Your current speed is', a.get_speed())

for x in range(5):
    a.brake()
    print('-- Your current speed is', a.get_speed())
    
    







