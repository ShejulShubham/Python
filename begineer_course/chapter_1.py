# 1. DATA TYPE
# this is the number data type
12846922541

# this is string data type (a string of characters - alphanumeric)
"my name is shubham"

'hello world'

# sub-objective (print out the string hello world)
print('hello world!') # print is a reserve keyword

# this is the list / array data type, contains a series or sequence of values that
# can be of any data type themselves
['eggs', 'banana', 
 "milk", 
 4, 
 []
 ]

# this is an object data type / dictionary
{
    "name": "shejul",
    "age": 28
} 

# boolean - True or False
True
False

# None - absence of information
None 

# a data type is a type of data that is friendly to python

# 2.0 Variables - a variable is a label for some data
number_of_eggs = 3

my_string = 'hello world'


print("variable number:",number_of_eggs)
print("variable string:", my_string)

print("multiplication in print:",number_of_eggs * 2)

# assigning to variables 
person = {
    "name": "shubham",
    "age": 28
}

shopping_list = [
    'banana',
    'apple',
    'guava',
    'grapes',
    5,
    []
]

print("object/dictionary person:",person)

# 3.0 Login and operations
# If block - if condition is true, execute the code, otherwise skip it
number_of_eggs = 6 # assigning new value

if number_of_eggs > 5:
    print('you have more than 5 eggs')
    
# print('we passed the if block')

if 'name' in person:
    print(person["name"])
else:
    print('the key name is not available within the person dictionary')
    
# if condition with reverse condition
    
if not 'banana' in shopping_list:
    print('Need to get bananas')
else:
    print('don\'t need bananas')
    
# Logical operators - and / or 

if number_of_eggs >= 5 and number_of_eggs <= 20:
    print('we also have less than 20 eggs so the egg range it between 5-20')
        
if number_of_eggs < 6 or number_of_eggs > 20:
    print('Okay, the number of eggs is outside of the ideal range which is 5-20')
    
# operators 
x = 3
y = 4
print(x * y + x - y / x)

# remainder operator (%)

remainder = y % x

print('remainder:',remainder)

# equality == (checks if the left is equal to right)
x == y # this would be false because x is 3 and y is 4 and therefore not equal
print(remainder == 10 % 3)


# not 
x != y # this would be true because x is not equal to y

if not number_of_eggs == 4:
    print(f'The number of eggs is not equal to four, but instead: {number_of_eggs}')
    
# loops (while / for)
count = 0
while count < number_of_eggs:
    print('hello')
    count = count + 1
    if count == 3:
        break
    
for x in shopping_list:
    print(x)
    
for i in range(10):
    print(i)
    
length_of_my_array = len(shopping_list)

for j in range(length_of_my_array):
    current_index = j
    current_value = shopping_list[j]
    print(f'current index is: {current_index} and the value at that index is {current_value}')
    
# functions

def print_funny_word(funny_word):
    '''this function takes an argument and print out the word provided as an argument,
    in addition to the word gilgamesh'''
    print('gilgamesh &', funny_word)
    
print_funny_word('doug')

def futile_work(work):
    '''this function is just going to return before the print statement'''
    return
    print(work)
    
for k in range(3):
    futile_work('make it')
    
def multiply_two_numbers(input1, input2):
    return input1 * input2

product = multiply_two_numbers(8, 9)
print(product)

# class

def jello():
    print('jello')

employee = {
    'age': 28,
    'action': jello
}

print(f'emp: {employee['action']()}')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def jello_two(self):
        print('jello jello')
        
new_person = Person('mark', 27)

new_person.jello_two()
print(new_person.name, new_person.age)


new_new_person = Person('lucy', 43)

