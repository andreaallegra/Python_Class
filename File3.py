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

    @classmethod
    # class method-constructor
    # class(cls) is always the first argument of a class method
    def from_string(cls, emp_str):
        # idea
        # 1 take the line first, last, pay = emp_str_1.split('-') and replace emp_str_1 with generic emp_str
        first, last, pay = emp_str.split('-')
        # 2 take the line new_emp_1 = Employee(first, last, pay) and replace Employee with cls
        new_emp = cls(first, last, pay)
        # and return the new employee object
        return new_emp

    @staticmethod # decorator
    # static method
    # take a date and return whether it is a workday
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False



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
# you can also run class methods from instances but it's never done: emp_1.set_raise_amt(1.05)

#class method as alternative constructor: create a new instance from a string
# example: we need to parse these strings
emp_str_1 = 'paolo-rossi-70000'
emp_str_2 = 'marco-blu-80000'
first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.first)
# now to avoid to parse all the time the employee string?
#  create a new constructor that we pass the string and create the instance from there
#  basically replacing the following files
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# results:
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.first)

#static method
import datetime
my_date = datetime.date(2016, 12, 31)
print(Employee.is_workday(my_date))