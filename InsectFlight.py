import InsectClass as i


mosquito = i.Insect(2,4)
housefly = i.Insect(3,5)

mosquito.flightLen()

housefly.flightLen()
print("the mosquito can fly up to", mosquito.get_miles(), "miles")
print("the housefly can fly up to", housefly.get_miles(), "miles")
