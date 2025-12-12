class Employee :
    raise_amount = 1.4
    num_of_emps=0
    def __init__(self,first,last,pay): #As constructor 1st parameter is the instance and called as "self"
        self.first = first
        self.last = last
        self.email = first+'@'+last+"ok.com"
        self.pay = pay
        Employee.num_of_emps+=1

    def get_full_name(self):
        return f"Full Name  - {self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(f"Start Total Employees {Employee.num_of_emps}")
emp_1 = Employee('Test1','M1',50000)
emp_2 = Employee('Test2','M2',60000)
print(f"Employee 1 Pay {emp_1.pay}")
emp_1.apply_raise()
print(f"Employee 1 Pay After Raise : {emp_1.pay}")
print(f"Raise Amount {Employee.raise_amount}")


#update on class level
Employee.raise_amount = 2
print(f"Raise Amount after {Employee.raise_amount}")


print(f"Total Employees {Employee.num_of_emps}")