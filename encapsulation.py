class Bank:
    def __init__(self):
        self.__intrest = 5

    def viewintrest(self):
        print(self.__intrest)

    def intresthike(self,intrest):
        self.__intrest = intrest

reservebank = Bank()

reservebank.viewintrest()

reservebank.__intrest = 7
reservebank.viewintrest()

reservebank.intresthike(9)
reservebank.viewintrest()