class Employee:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    @staticmethod
    def from_string(parse_stirng):
        firstname, lastname, salary =  parse_stirng.split("-")
        return Employee(firstname, lastname, int(salary))
        

emp1 = Employee("Mary", "Sue", 60000)
print(emp1.firstname)
print(emp1.salary)

emp2 = Employee.from_string("John-Smith-55000")
print(emp2.firstname)
print(emp2.lastname)
print(emp2.salary)
