class Car(object):
    def speed(self):
        print(" car goes faster ")

class ferrari(Car):
    def speed(self):
        print("ferrari is the fastest car")

ob = ferrari()
ob.speed()