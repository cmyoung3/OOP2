import RetailItem as ri

desc = "Jacket"
inv = 12
price = 59.95


#Item 1
Item1 = ri.RetailItem(desc,inv,price)


print("Desc | Inv | Price")
print(Item1.get_Description(), Item1.get_Inventory(), Item1.get_Price(), sep=' | ')

#Item 2

desc = "Designer Jeans"
inv = 40
price = 24.95

Item2 = ri.RetailItem(desc,inv,price)
print(Item2.get_Description(), Item2.get_Inventory(), Item2.get_Price(), sep=' | ')

#Item 3

desc = "Shirt"
inv = 20
price = 24.95

Item3 = ri.RetailItem(desc,inv,price)
print(Item3.get_Description(), Item3.get_Inventory(), Item3.get_Price(), sep=' | ')



    