import StudentClass as sc

studentid = 1001
name = 'Caleb'
dob = '1/1/2000'
classification = 'senior'

caleb = sc.Student(studentid,name,dob,classification)

caleb.calc_age()

caleb.register()

print("Student age is:", caleb.get_age())
print("Student can register betwee:",caleb.get_registration())
