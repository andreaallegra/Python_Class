https://www.youtube.com/watch?v=ZDa-Z5JzLYM
https://www.youtube.com/watch?v=BJ-VvGyQxho
https://www.youtube.com/watch?v=rq8cL2XMM5M
https://www.youtube.com/watch?v=RSl87lqOXDE
https://www.youtube.com/watch?v=3ohzBxoFHAY
https://www.youtube.com/watch?v=jCzT9XFZ5bw
https://www.youtube.com/watch?v=FsAPt_9Bf3U

When we talked about data and functions that are associated with a specific class we call them attributes and methods
method: is a function associated with a class

now let's create a simple class
a class is a blueprint for creating instances

instance variables and class variables are different

instance variables contains data that are specific for a class instance 

now let's create a __init__ method within the class (the init method is the constructor)
when you create methods within a class they receive the instance as the first argument automatically
and we should call the instance self

names, pay, e-mail are attributes of the class
now if we want to perform some actions we need to add some methods to the class
idea: show full name of the employee: how? asking a class method to do so
remember to always pass the instance name (self) as a first argument of the method definition:
this what happens if you don't pass self:fullname() takes 0 positional arguments but 1 was given
because the instance name is pass automatically

next: difference between class variables and instance variables