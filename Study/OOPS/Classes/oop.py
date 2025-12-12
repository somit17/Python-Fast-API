 #Python Object-Oriented Programming

class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Test1'
emp_1.last = 'M'
emp_1.email = 'test1@ok.com'
emp_1.pay = 50000


emp_2.first = 'Test2'
emp_2.last = 'M'
emp_2.email = 'test2@ok.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)



class Emp :
    def __init__(self,first,last,pay): #As constructor 1st parameter is the instance and called as "self"
        self.first = first
        self.last = last
        self.email = first+'@'+last+"ok.com"
        self.pay = pay

    def get_full_name(self):
        return f"Full Name  - {self.first} {self.last}"



employee = Emp('Test1','M',50000)
print(employee.email)
print(employee.get_full_name())
print(Emp.get_full_name(employee)) #Same as above


