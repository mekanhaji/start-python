# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits=('Apples','Oranges','Grapes') 

# Using tuple constructor
fruits_cons=tuple(('Apples','Oranges','Grapes'))

# Single value needs trailing comma(,)
fruits2=('Apples',)

# Get value
print(fruits[1]) # Output -> Oranges

# Can't change value 
fruits[0]='Pears' # Output ->  TypeError: 'tuple' object does not support item assignment

# Delete tuple
del fruits2 # print(fruits2) ->NameError: name 'fruits2' is not defined.
# print(fruits2)

# Get length
print(len(fruits)) # Output -> 3

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set ={'Apples', 'Oranges', 'Mango'}
 # print(fruits_set) -> {'Apples', 'Oranges', 'Mango'}
# Check if in set
print('Apples' in fruits_set) # Output -> True

# Add to set
fruits_set.add('Grape') # Output -> {'Grape', 'Apples', 'Oranges', 'Mango'}

# Remove from set
fruits_set.remove('Apples') # Output -> {'Grape', 'Oranges', 'Mango'}

# Clear set
fruits_set.clear() # Output -> set() 

# Delete set
del fruits_set

print(fruits_set) # Output -> NameError: name 'fruits_set' is not defined.