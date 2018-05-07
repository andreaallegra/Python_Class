
class Employee:

    # class variables
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # the init method run every time we create a new employ (new instance)
        self.first = first  # this is the same as writing emp_1.first = 'Corey'
        self.last = last # instance variables
        self.pay = pay
        self.email = first + '.' + last + "@employee.com"
        Employee.num_of_emps += 1 # and here I don't use self.num_of_emps as we did for self.raise_amount

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # self.pay = int(self.pay * 1.04) substituted by
        # self.pay = int(self.pay * raise_amount)
        # this gives an error because if we need to access the instance variable we need to access through the class itself:
        # self.pay = int(self.pay * Employee.raise_amount)
        # or through the instance of the class
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps) # return 2 because it incremented twice then we instantiated our emp_1 and emp_2

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# why we can get access to a class variable through the instance of the class?
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# I can access this class variable through the class itself as well as from both instances
# because when we try to access an attribute on an instance it will first check if the instance contains that attribute
# and it if doesn't it check if the class or any class that it inherits from contains that attribute
# so when we access raise_amount from the instances they don't have that attribute but they inherit it from the class
# attribute
# now print out the namespace of emp_1
print(emp_1.__dict__)
print(Employee.__dict__)
# the class contains the raise_amount attribute
# and that's the value that the emp_1 instance see when we access that attribute from the instances (emp_1.raise_amount)
Employee.raise_amount= 1.04
# this change the amount for the class and for the instances
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount= 1.05 # this create the raise_amount attribute within emp_1 and I can see the attributes using dict
# so it finds it within its namespace before going and searching the class
# and we didn't see raise_amount for emp_2 for it still falls back to the class raise_amount
print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# from this is clear that using self.raise_amount or Employee.raise_amount at line 21 is different
# using self.raise_amount gives the possibility of change the value of raise_amount for an instance as we just did