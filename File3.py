# https://www.youtube.com/watch?v=rq8cL2XMM5M

class Employee:

    # class variables
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # the init method run every time we create a new employ (new instance)
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@employee.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    # this alter the method functionality so that we receive the class rather than the instance as the first argument
    # within a regular method we call this instance variable "self", and the name of the class variable is "cls"
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount # amount is the value we accept from this method

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# now I want to change the raise_amt:
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# and all have changed because we run the set_raise_amt method which is a class method
# and we are setting the class variable raise_amt to 5%

#Employee.set_raise_amt(1.05) same as Employee.raise_amount = 1.05