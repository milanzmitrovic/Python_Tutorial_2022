

# Homeworks:

# *** When working with integers in homework,
#     always choose integers greater than 300.

# 1. Create 10 variables that are going to hold integer objects.

a1 = 33
a2 = 44
a3 = 55

# ------------------------------------------------------------------------------------------------ #

# 2. Create 10 variables that will store float objects.

b1 = 11.1
b2 = 22.2
b3 = 33.3

# ------------------------------------------------------------------------------------------------ #

# 3. Create 10 variables that store string objects.

c1 = '123'
c2 = '456'
c3 = '789'

# ------------------------------------------------------------------------------------------------ #

# 4. Create 20 variables that store any data type (inf, float, str), but
# use not valid Python variable name. Here we expect to receive Python errors.

1a = 11
@b = 77
!c = 300

# ------------------------------------------------------------------------------------------------ #

# 5. Create 2 variables that are storing two different references to integer
# objects. Check if two objects have same value.

my_int_1 = 400
my_int_2 = 400

my_int_1 == my_int_2

id(my_int_1) == id(my_int_2)

# ------------------------------------------------------------------------------------------------ #

# 6. Create 2 variables that are storing reference to same integer object.
# Confirm that both variables are pointing to same object.
# Confirm that 'both' objects have same value.

my_int_3 = 500
my_int_4 = my_int_3

my_int_3 == my_int_4

id(my_int_3) == id(my_int_4)

# ------------------------------------------------------------------------------------------------ #

# 7. Create arbitrary string of at least 20 characters.
# Name it as 'my_string_variable'.

my_string_variable = "123456789a123456789b"

# ------------------------------------------------------------------------------------------------ #

# 8. Check length of my_string_variable.
# Print length of my_string_variable.

print(len(my_string_variable))

# ------------------------------------------------------------------------------------------------ #

# 9. Print ID of my_string_variable.

print(id(my_string_variable))

# ------------------------------------------------------------------------------------------------ #

# 10. Create new variable named my_string_variable_2 that
# are going to store reference to same object as my_string_variable.

my_string_variable_2 = my_string_variable

# ------------------------------------------------------------------------------------------------ #

# 11. Check if data to which our variables are pointing (my_string_variable and my_string_variable_2),
# are equal.

my_string_variable == my_string_variable_2

# ------------------------------------------------------------------------------------------------ #

# 12. Check if our objects ((my_string_variable and my_string_variable_2)
# are pointing to same object/data.

id(my_string_variable) == id(my_string_variable_2)

# ------------------------------------------------------------------------------------------------ #

# 13. Create new string. Name it my_favourite_string.
# Check ID of that string.

my_favourite_string = 'my favourite string'

id(my_favourite_string)

# ------------------------------------------------------------------------------------------------ #

# 14. Create new string my_favourite_string_2.
# Variable my_favourite_string_2 should point to different
# object/data, but it should have same value as my_favourite_string.

my_favourite_string_2 = 'my favourite string'

# ------------------------------------------------------------------------------------------------ #

# 15. Prove that you correctly created solution to exercise 14.

id(my_favourite_string) == id(my_favourite_string_2)
my_favourite_string == my_favourite_string_2

# IDs and references becomes very important when dealing with mutable data types.
# For immutable data types, it does not make any difference. But it is good to learn
# and practice it now.
# --->>
# The same strings have the same ids. But Python is not guaranteed to intern strings.
# If you create strings that are either not code object constants or contain characters
# outside of the letters + numbers + underscore range, you'll see the id() value not being reused.
# --->>

# ------------------------------------------------------------------------------------------------ #

# 16. Take first 5 characters form string whose reference/ID is
# stored in my_string_variable.

my_string_variable[:5]

# ------------------------------------------------------------------------------------------------ #

# 17. Take last 10 characters from string whose reference/ID is
# # stored in my_string_variable.

my_string_variable[-10:]

# This task can also be written:
#   Take last 10 characters from variable my_string_variable.
#   Or, take last 10 characters from string stored in my_string_variable.

# ------------------------------------------------------------------------------------------------ #

# 18. Take everything from my_string_variable, but not first 3 characters.

my_string_variable[3:]

# ------------------------------------------------------------------------------------------------ #

# 19. Take everything, but not last 3 characters from my_string_variable.

my_string_variable[:-3]

# ------------------------------------------------------------------------------------------------ #

# 20. Take characters from position 5 (including 5th character) up to
# (and including) character 17.

my_string_variable[4:17]

# ------------------------------------------------------------------------------------------------ #

# 21. Take string characters from position 15 (including 15th character) and
# up to position 10 (including 10th character).
# Tip: you should do inverse slicing sth like [-6: -4]

my_string_variable[-11:-5]
my_string_variable

# ------------------------------------------------------------------------------------------------ #

# 22. Reverse string stored in my_string_variable.

my_string_variable[::-1]

# ------------------------------------------------------------------------------------------------ #

# 23. Create 10 examples (use cases) with f-strings.

bgd = 'Belgrade'
ns = 'Novi Sad'
n = 'Nis'

f"My favourite city is {bgd}."
f"My favourite city is {ns}."
f"My favourite city is {n}."

# ------------------------------------------------------------------------------------------------ #

