class Vehicle(object):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def viewvehicle(self):
        print(self.brand)
        print(self.model)

class Bike(Vehicle):
    def __init__(self,brand,model,cc,price):
        self.cc = cc
        self.price = price
        Vehicle.__init__(self,brand,model)

    def displaybike(self):
        print("The brand is :",self.brand)
        print("The model is :",self.model)
        print("The cc is :",self.cc)
        print("The price is :",self.price)

x = Bike("yamaha","R15v3","155cc","186000")
x.displaybike()
x.viewvehicle()

y = Vehicle("yamaha","R15v3")
y.viewvehicle()