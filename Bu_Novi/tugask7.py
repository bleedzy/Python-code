class Employee:
    empCount = 0

    def __init__(self, name, salary): 
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee : ", Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)
    
if __name__ == "__main__":
    e1 = Employee("Ibnu", 4000)
    e2 = Employee("Gogon", 5000)

    e1.displayEmployee()
    e2.displayEmployee()

    e1.displayCount()