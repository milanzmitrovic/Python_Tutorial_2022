
### Data types
- Simple data types: integer, float, string.
- Componnd data types: list, tuple, dictionarty, set.


### Useful functions:

- print()
- id()
- type()
- len()


### Integers
- int()


### Floats
- float()


### Boolean
- True/False


### Strings
- str()


### Comments


### Variables
- When we want to store or save for later some data.
- Variables are used for labeling data.
- Variable assignment (simple and multiple)



### String methods
- .count()
- .replace()
- .join()
- .split()
- .partition()
- .islower()
- .isupper()
- .capitalize()
- .upper()
- .lower()
- .strip()
- .lstrip()
- .rstrip()


### 'in' and 'not in' operator


### String operators
- Addition 
- Multiplication

### Integer/float operators
- Addition
- Subtraction
- Multiplication
- Division
- Modulo
- Exponentiation


### String indexing and slicing


### f-Strings

### What is object in Python?
- Theoretical idea
- Practical point of view

### Comparing Python objects
- Comparing if objects contains same value
- Comparing if two variables refers to same object
- Comparing float objects




```python


# --> 1. Create data and store it into variable.
milan_favourite_car = 'BMW'

# Three things happened here:
# a) Some data are created - string with value of 'BMW'.
# b) Python creates ID i.e. object reference for that data.
# c) Python connects/assigns ID created in step 'b)' to name
#   that is on left side of equation 'milan_favourite_car'.


# WHat happens when we call variable?
# In other words, when we type milan_favourite_car
# and execute this command?
#   - A) We call variables and we want to see what
#       value this specific variable is keeping.
#   - B) Python interpreter tries to find which ID (object reference)
#        is stored in this variable.
#   - C) Python interpreter searches for object/data that has this specific ID
#       and returns it.


# What we did here?
# - We created data of type string 'BMW'.
# - We gave name to that data i.e.
#   we labeled that data. Data in this
#   case is 'BMW'.

# What does 'storing data into variable mean?
# - When data is created, Python creates ID
#   of that data.
# - Then, ID is stored into variable.
# - Another name for ID is 'object reference'.

# Another way of thinking:
# - Variable assignment is nothing else but
#   getting object reference from right side of equation
#   and putting/connecting it to name that is on the left side of equation.

# In other words, variables is used for naming objects
# in human-readable format.

# Python interpreter keeps record of data/objects by ID (object reference),
# while, we humans, are better in naming things with written words.

# Object/data --> ID (object reference) --> variable name.

# There are two cases:
# A) When we create NEW data/object on right side of equation.
my_favourite_car = 'BMW'

# B) When we have variables on both sides of equation.
#   We just pass reference that is stored in variable on the right to
#   variable on the right.
#   id of my_favourite_car is going to be stored in variable your_favourite_car
#   i.e. both variables will be storing same ID.
your_favourite_car = my_favourite_car
print(id(my_favourite_car) == id(your_favourite_car))


# --> 2. Python is 'pass by reference' language by design.
# What does that mean?
# - We are passing reference of object/data that is on right side of equation
#   to the variable name that is on left side of equation.
# - After that process, both sides of equation will have same ID.


# --> 3. How to get object/data if we know its ID?
# Bear in mind that this is almost never done in regular practice
# of programming, but it is useful to prove some of our hypothesis.
import ctypes
a = "hello world"
b = a
print(ctypes.cast(id(a), ctypes.py_object).value)

del b
print(ctypes.cast(id(a), ctypes.py_object).value)

del a
print(ctypes.cast(id(a), ctypes.py_object).value)

# --> 4. Reassigning values to variable
# Only last thing matter.
#

a = 500
a = 700
print(a)
print(id(a))


# --> 5. Switching values between variables

# a) Data is created (integer 300).
# b) Python internally creates ID/reference for that data.
# c) That ID/reference is connected to name of variable (x in our example).
x = 300

# There is variable on both sides of equality sign.
# Python internally asks what ID/reference is stored into
# variable on right, then it stores same reference under
# variable on left side.
y = x


# New data/object is created (integer 400) and
# ID/reference to that object is stored under
# name X i.e. in variable named X.
# There was already some ID/reference stored under X.
# Python delete it and stores new ID/reference in
# variable on left side of equation.
x = 400
print('x', x)
print('y', y)


# --> 6 Deleting variable
# Firstly, lets answer what is variable?
# Variable is storage container for ID of object/data.
# When we delete variable, we are not deleting data/object,
# we just delete ID that was stored under that specific variable.

a = 77
print(id(a))
del a
# Following line will produce error:
print(id(a))

# Let's recall our example with man that has more than one name.
# Imagine chinese man came to US to study. His original name is
# difficult to pronunciate, so they gave him new name, John. When
# he changes class, they give him another common international name.

original_name = 'Haoyu'
john = original_name
peter = original_name

print(id(original_name))
print(id(john))
print(id(peter))

# When chinese student moves from US to EU, we will delete his US name.
del john
print(id(original_name))
print(id(peter))

# But, data/object with string 'Haoyu' will continue to exist.
# Question is until when?
# - IT WILL EXIST AS LONG AS, AT LEAST ONE VARIABLE IS STORING
# REFERENCE TO THAT OBJECT.

# In our example with chinese student, we can also delete his original name.
# But string 'Haoyu' will continue to exist as long as variable peter exists.
del original_name
print(id(peter))


# --> 7. What is another way to think
#        about variable assignment?

# There are 3 elements in story:
# 1. Data/object
#       - Data/object is sth that is stored somewhere
#         in memory (memory access is controlled by
#         Python interpreter).

# 2. ID i.e. object reference
#       - Whenever some new data/object is created,
#         Python creates some number that is going
#         to be tied to that newly created data/object.
#         This number is going to be unique i.e. there
#         will never be two data/objects with same ID.

# 3. Variable
#       - We as a humans are not so good at remembering numbers.
#         So, we tend to use letters and names for naming purpose.
#       - Instead of using internal Python way for naming data/objects,
#         we are going to name it with words.
#       - We can think about variable in following way:
#               a) Create one box.
#               b) Put ID of object in that box.
#                  PAY ATTENTION: WE ARE NOT PUTTING OBJECT/DATA
#                  INTO BOX, WE ARE PUTTING ID i.e. OBJECT REFERENCE
#                  TO OUR BOX!!!
#               c) Put name on that box i.e. label box.
#        - Name that we used to label box in step 'c'
#          is variable.
#        - In other words, variable is name of box in which we
#          put object's ID.
#          PAY ATTENTION: NAME OF THE BOX IN WHICH WE PUT OBJECT/DATA
#          DOES NOT EXIST IN PYTHON. THIS TERM IS NOT DEFINED.
#          IN SOME OTHER LANGUAGES IT EXISTS, IN PYTHON IT DOES NOT!

# --> So workflow is following:
#       data/object >> ID i.e. object reference >> variable name.


# --> 8.
# Giving new name to already existing data/object
#               VS
# Creating new data and giving it a name.


# --> 9.
# Deleting variable
#               VS
# Deleting underlying data/object

# How to delete variable?
# i.e. how to delete name of data/object?
# --> We can use 'del' keyword to do so.
#     In this case, we will delete box
#     that was used to store ID of object/data,
#     not the underlying data itself.

#     [Previous sentence is semi-true. Why?
#      Because if variable that we are deleting
#      is last variable that is storing ID
#      of specific data/object, then this specific
#      object/data will be deleted also.
#      If there is any other variable that is
#      storing ID of specific object/data, then
#      underlying object/data will NOT be deleted.]

# How to delete underlying data?
# When are underlying data deleted?
# --> When there is no more variables
#     that are storing ID of specific
#     data/object, then data/object will
#     be automatically deleted from
#     Python memory.


# --> 10.
#
# !!!Creating new data
# 		VS
# Giving another/additional data to already existing data!!!
#
#
#
# Equality of variables!!!
#
# a = 300
# b = a
#
# a==b
# # True
#
# id(a) == id(b)
# # True
#
#
# —> Case 1: Both variables are pointing to same data/object.
# 		In other words, both variables have same ID.
# 		In other words, one object/data has two names.
#
#
# —> Case 2: Variables are pointing to different data/object.
# 		In other words, variables have different IDs.
# 		In other words, those are two object/data with two
# 		different names.
#
# a = 300
# b = 300
#
# a==b
# # True
#
# id(a) == id(b)
# # False
#
# Two different terms:
# 	- value of object/data
# 	- ID of object/data
#
# Comparison operator (==) is checking if object/data whose ID is
# stored in variable on left side has same/equal/identical value as
# object/data whose ID is stored in variable on right side of equation.
#
#
# We introduce new term: ‘Value that is stored in some variable’.
# We know that this definition is not 100% correct, since we are NOT
# storing data/object into/under variable (we are storing object/data ID),
# we will use this term/definition since it is well accepted/present in
# python community.
# It is data/object whose ID is stored in box named with variable name.
#
#


# --> 11. '==' VS 'is' operator.
# 'is' operator is checking if two variables
# are referencing same object.
# 'a is b' is same as 'id(a)==id(b)

# '==' operator is checking if underlying
# data are the same.
# Underlying data can be stored on two 
# different places in memory or they can be 
# same object/data.

# If 'is' operator returns True, then '=='
# operator will always return True.
# Reverse is not true i.e. if '==' operator
# returns True, 'is' operator can return
# True, but it is not guaranteed to be True.



# 
# !!!Creating new data 
# 		VS 
# Giving another/additional name to already existing data!!!
# 
# 
# 
# Equality of variables!!!
# 
# a = 300
# b = a
# 
# a==b
# # True
# 
# id(a) == id(b)
# # True
# 
# 
# —> Case 1: Both variables are pointing to same data/object.
# 		In other words, both variables have same ID.
# 		In other words, one object/data has two names. 
# 
# 
# —> Case 2: Variables are pointing to different data/object.
# 		In other words, variables have different IDs.
# 		In other words, those are two object/data with two 
# 		different names.
# 
# a = 300
# b = 300
# 
# a==b
# # True
# 
# id(a) == id(b)
# # False
# 
# Two different terms:
# 	- value of object/data
# 	- ID of object/data
# 
# Comparison operator (==) is checking if object/data whose ID is
# stored in variable on left side has same/equal/identical value as 
# object/data whose ID is stored in variable on right side of equation.
# 
# 
# We introduce new term: ‘Value that is stored in some variable’.
# We know that this definition is not 100% correct, since we are NOT
# storing data/object into/under variable (we are storing object/data ID),
# we will use this term/definition since it is well accepted/present in 
# python community.
# It is data/object whose ID is stored in box named with variable name.
# 
# 
# 





```








