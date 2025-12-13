class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    #kind of method overloading
    def __repr__(self): #Debugging and Logging
        return f"Employee: - {self.first} , {self.last} , {self.pay}"


    def __str__(self):
        return  f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return  self.pay+other.pay

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)
#repr(emp_1)
#str(emp_1)
print(emp_1 + emp_2)

#print(len(emp_1))