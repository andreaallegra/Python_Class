

class Employee:
    def __init__(self, first, last, pay):
        self.first = first  #this is the same as writing emp_1.first = 'Corey'
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@employee.com"

    def fullname(self):
        # and use the same login as the first approach
        return '{} {}'.format(self.first, self.last)



# instances of Employee class

# old (before the __init__ method
#emp_1 = Employee()
#emp_2 = Employee()

# new (after the __init__ method
# now we can pass the values that we specified in the init method,
# excluding the instance because the instance is pass automatically
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#when these lines are read the __init__method gets called and create all the instance variable:
# self.first = Corey...
# and now we can delete this manual assignments below

print(emp_1)
print(emp_2)


# emp_1 and emp_2 are Employee objects

# create a instance variable (instance variable contains data that are specific to a class instance)

# emp_1.first = 'Corey'
# emp_1.first = 'Schafer'
# emp_1.email = 'Corey.Schafer@employee.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.first = 'User'
# emp_2.email = 'Test.User@employee.com'
# emp_2.pay = 60000

print(emp_1.email)

# and now within the __init__ method I am going to see all the instance variables

#idea; show full name.
# first approach
print('{} {}'.format(emp_1.first, emp_1.last))
#2 second: create a class method
print(emp_1.fullname())
# look that we need to add the () because this is a method instead of an attribute
# I don't need to pass the instance name because it's passed automatically

# you can run the method using the class name itself
# and here I need to explicitly the instance name as an argument because it doesn't know the instance which we want
# to run the method with
print(Employee.fullname(emp_1))

