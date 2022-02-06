# Strings in python are surrounded by either single('') or double("") quotation marks. Let's look at string formatting and some string methods

name ='kanhaji'
age=20

#1. String Formatting
    #1.1 Concatenate

# print("My name is "+name+" and i am "+str(age)+" year old")# Output-> My name is kanhaji and i am 20 year old
    #Here,As int and str can't concatenate. we used typecasting on age variable to change it into str.

    #1.2 Argument by position

# print('Hello My name is {arg1} and i am {arg2} year old'.format(arg1=name,arg2=age))
    # Output -> My name is kanhaji and i am 20 year old
    # here, we make two arguments in our str i.e. arg1 and arg2.
    # using format() method we assign it to our variable.


    # 1.3 F-string (Only with Python3.6+)
# print(f"Hello, My name is {name} and i'm {age}")
    # Output -> Hello, My name is kanhaji and i'm 20

# String Methods 

string='hello people'

#1. Capitalize string
print(string.capitalize())# Output -> Hello people
    #Makes first word capital in string
     
#2 Make all uppercase
print(string.upper()) # Output -> HELLO PEOPLE
    # Makes all words upper case in string

#3 Make all lower
print(string.lower())# Output -> hello people
    # Makes all words lower case in string

#4 Swap case
print(string.swapcase())# Output -> HELLO PEOPLE
    # Changes case if lower -> upper and if upper -> lower 

#5 Get length
print(len(string))# Output -> 12
    # len() return the length of objects(in this case string)

#6 Replace
print(string.replace('people', 'everyone'))# Output -> hello everyone
    # replece words

#7 Count
sub = 'h'
print(string.count(sub))# Output -> 1
    # return frequecy of word in string

#8 Starts with
print(string.startswith('hello'))# Output -> True

#9 Ends with
print(string.endswith('d'))# Output -> False

#10 Split into a list
print(string.split())# Output -> ['hello', 'people']

#11 Find position
print(string.find('r'))# Output -> -1