'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''
# <- using this(hasetag) we can make single line comment

# A variable is a container for a value, which can be of various types
# defining variable are easy in python

your_name = 'kanhaJi' #here, I have defining a variable named "your_name" of type String
# In Python we don't have to defining datatype of variable
# we can check type of a variable using 'type()' function
# print() function in python used for outputing value on conlose.
print(type(your_name)) # Output -> <class 'str'>


"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore( _ )
  - Can have numbers but can not start with one
"""
"""
Data types in Python:
  -Number Data Type :
    -int ex. 1,12,585281,...
    -float ex. 12.0,1.0.1.25,..
  -Characters Data Type:
    -String | str ex. 'hello',"world!"
"""
a = 5
print(a, "is of type", type(a))# Output -> 5 is of type <class 'int'>

a = 2.0
print(a, "is of type", type(a))# Output -> 2.0 is of type <class 'float'>

a = 'hello'
print(a, "is of type", type(a))# Output -> hello is of type <class 'str'>

"""
Type Casting In Python:
  - we can change data type of a variable after defining it.
  - to change it into int -> int()
  - to change it into float -> float()
  - to change it into string ->str() 
"""
int_number = 123
print(int_number," is type of ",type(int_number))# Output -> 123  is type of  <class 'int'>
change_into=float(int_number) 
print(change_into," now ",type(change_into))# Output -> 123.0  now  <class 'float'>