class Worker_17:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname =surname
        self.__rate = rate
        self.__days = days

    def getSalary(self,__rate, __days):
        self.salary = __rate * __days
        return self.salary

    def printInfo(self, __name, __surname, __rate, __days ):
        print( self.__name, self.__surname, self.__rate, self.__days, self.salary)

class Premium(Worker_17):
    def __init__(self, salary):
        super().__init__(salary)
    def getSalary(self,__rate, __days):
        premium = 2000
        if self.__rate > 500 and __days >25:
            return self.salary == __rate * __days + premium

    worker1 = Worker_17('Алеша','попович', 200, 6)
    worker2 = Worker_17('добрыня','никитич', 600, 26)
    worker1.getSalary(200, 6)
    worker2.getSalary(600, 26)
    worker1.printInfo('Алеша','попович', 200, 6)
    worker2.printInfo('добрыня','никитич', 600, 26)








