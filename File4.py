#https://www.youtube.com/watch?v=RSl87lqOXDE


class Employee:

    # class variables
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # the init method run every time we create a new employ (new instance)
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# subclass that inherit from the Employee parent class
# just by inherit the subclass will have all the attributes and methods of the parent class
class Developer(Employee):

    # idea: customize the pay raise for the developer
    raise_amount = 1.10

    # idea customize the instantiation only for the Developer instance
    def __init__(self, first, last, pay, prog_lang):
        # idea: let the Employee class to handle all the Employee attributes
        super().__init__(first, last, pay)
        # same as (more complex)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


# another subclass which inherit from Employee
class Manager(Employee):
    # idea: pass a series of employees that the manager supervises
    def __init__(self, first, last, pay, employees=None):
        # note don't pass an empty list as default argument instead of None
        # but you don't want to pass mutable data type as def arguments
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # instance method
    # idea: ability to add or remove from the list of employee that the manager supervise
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # print out all the employees that the manager supervise
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


# when we instantiate our Developer it first look in the Developer class
# for the init method and if it doesn't find it will walk up the chain of
# inheritance until it finds what it is looking for
# and this chain # is called method resolution order
dev_1 = Developer('Corey', 'Schafer', 50000, "python")
dev_2 = Developer('Blue', 'Pipper', 50000, "java")
emp_2 = Employee('Test', 'User', 60000)

print(dev_1.first)
print(emp_2.first)

# print(help(Developer))
# so when we instantiate our Developer (by creating our two new developers)
# Python first look in Developer class for the init method
# and if it cannot find it it search it in the Employee class
# and if hadn't find there it would have looked in the builtins.object class

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
# after creating the class variable raise_amount in the Developer class it will
# use that specific amount rather than the Employee raise_amount
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)
# but it will not affect the raise_amount for the Employee class

print(dev_1.prog_lang)

mgr_1 = Manager('paul', 'redcliff', 40000, [dev_1])
print(mgr_1.first)
print(mgr_1.fullname())

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))
print(issubclass(Manager,Manager))
