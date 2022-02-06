# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
number_list=[1,2,3,4,5]
fruits=['Apples','Oranges','Grapes','Pears']

# Using list Constructor
same_number_list=list((1,2,3,4,5))

# print(number_list,same_number_list)
# Output ->[1, 2, 3, 4, 5] [1, 2, 3, 4, 5]

# Methods of list

# Get Value
print(fruits[0]) # Output -> Apples 

# Get the last value
print(fruits[-1]) # Output -> Pears

# Get length
print(len(fruits)) # Output -> 4

# Append to list
fruits.append('Mangos') # print(fruits) -> ['Apples', 'Oranges', 'Grapes', 'Pears', 'Mangos']

# Remove from list
fruits.remove('Grapes') # print(fruits) -> ['Apples', 'Oranges', 'Pears', 'Mangos']

# Insert into position
fruits.insert(2,'Strawberries') # print(fruits) -> ['Apples', 'Oranges', 'Strawberries', 'Pears', 'Mangos']

# Change value ,this will rewrite value at index 0(which is Apples)
fruits[0]='Blueberries' # print(fruits) -> ['Blueberries', 'Oranges', 'Strawberries', 'Pears', 'Mangos']

# Remove with pop
fruits.pop(2) # print(fruits) -> ['Blueberries', 'Oranges', 'Pears', 'Mangos']

# Reverse list
fruits.reverse() # print(fruits) -> ['Mangos', 'Pears', 'Oranges', 'Blueberries']

# Sort list
fruits.sort() # print(fruits) -> ['Blueberries', 'Mangos', 'Oranges', 'Pears']

# Reverse sord
fruits.sort(reverse=True) # print(fruits) -> ['Pears', 'Oranges', 'Mangos', 'Blueberries']

print(fruits)