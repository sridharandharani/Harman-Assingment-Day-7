# create a class hospital and display the doctor details from user
class Hospital:
    def __init__(self,name,age,qualification,salary):
        self.name = name
        self.age = age
        self.qualification = qualification
        self.salary = salary

    def viewdoctor(self):
        print("The doctor name is",self.name)
        print("The doctor age is",self.age)
        print("The doctor qualification is",self.qualification)
        print("The doctor salary is",self.salary)

getname = input("Enter the name :")
getage = input("Enter the age :")
getquali = input("Enter the qualification :")
getsalary = input("Enter the salary :")

output = Hospital(getname,getage,getquali,getsalary)
output.viewdoctor()