# If/ Else conditions are used to decide to do something based on something being true or false
x = 21
y = 20
if x>y:
    print(f'{x} is greater then {y}') # Output -> 21 is greater then 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values
x,y=20,20
if x>y:
    print(f'{x} is greater then {y}') # Output -> 21 is greater then 20
elif x==y:
    print(f'{x} is equal to {y}') # Output -> 20 is equal to 20
x,y=20,10
if x!=y:
    print(f'{x} is not equal to {y}') # Output -> 20 is not equal to 10

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')  # Output -> 20 is greater than 2 and less than or equal to 10

# or
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 or less than or equal to 10')  # Output -> 20 is greater than 2 or less than or equal to 10

# not
if not(x == y):
  print(f'{x} is not equal to {y}')  # Output -> 20 is not equal to 10


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
x=3
numbers = [1,2,3,4,5]

#  in
if x in numbers:
  print(x in numbers)  # Output -> True
x=6
# not in
if x not in numbers:
  print(x not in numbers)  # Output -> True


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is
if x is y:
  print(x is y)  # Output -> False

# is not
if x is not y:
  print(x is not y) # Output -> True