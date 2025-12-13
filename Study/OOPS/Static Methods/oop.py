class Employee:
    raise_amt = 1.4

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    #Class Method to update class Variable
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    #Alternative constructor
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)

    #Static Method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return  False
        return True


emp_1 = Employee('Test','M1',4000)
print(f"Before Employee Raise Amount  = {emp_1.raise_amt}")


#calling Class Method
Employee.set_raise_amt(2)
print(f"After class method calling Employee raise amount  = {emp_1.raise_amt}")



emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')
#new_emp_1 = Employee(first, last, pay)


new_emp_1 = Employee.from_string(emp_str_1)
print(f"Employee After class method calling Name - {new_emp_1.first} ")


print(f"Calling Static Method below")
import datetime
my_date = datetime.date(year=2025,month=12,day=12) #Change value to 13 returns False

print(f"Employee Working Day  : {Employee.is_workday(my_date)}")