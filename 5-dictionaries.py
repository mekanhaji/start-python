# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person ={
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
# print(person) -> {'first_name': 'John', 'last_name': 'Doe', 'age': 30}

# Using dict constructor
person2 = dict(first_name='Sara', last_name='Williams')
# print(person2) -> {'first_name': 'Sara', 'last_name': 'Williams'}

# Get value
print(person['first_name'])# Output -> John
print(person.get('last_name'))# Output -> Doe

# Add key/value
person['phone'] = '555-555-5555' 
 # print(person) -> {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'phone': '555-555-5555'}

# Get dict keys
print(person.keys()) # Output -> dict_keys(['first_name', 'last_name', 'age', 'phone'])

# Get dict items
print(person.items()) # Output -> dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 30), ('phone', '555-555-5555')])

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston' # Output -> {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'phone': '555-555-5555', 'city': 'Boston'}


# Remove item
del(person['age'])
person.pop('phone') 

# Clear
person.clear() # Output -> {}

# Get length
print(len(person2)) # Output -> 5

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]
# Output -> [{'name': 'Martha', 'age': 30}, {'name': 'Kevin', 'age': 25}]

print(people[1]['name']) # Output -> Kevin