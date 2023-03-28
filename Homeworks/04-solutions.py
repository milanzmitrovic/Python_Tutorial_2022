

# 1. Write a Python program that starts with two dictionaries
# and creates a new dictionary containing only the key-value
# pairs that are common to both dictionaries.

# Tips: Generate starting dictionaries by yourself.


dictionary_1 = {
    'name': 'Milan',
    'surname': 'Mitrovic',
    'age': 31
}

dictionary_2 = {
    'name': 'Milan',
    'surname': 'Mitrovic',
    'age1': 31
}

new_dictionary = dict()

for key in dictionary_1.keys():

    try:
        if dictionary_1[key] == dictionary_2[key]:
            new_dictionary[key] = dictionary_1[key]
    except KeyError:
        print(f'Desio se KeyError prilikom {key}')


new_dictionary

# ------------------------------------------------------------------------------------------------ #

# 2. Write a Python program that starts with a list of dictionaries
# and returns a new list containing only the dictionaries where
# the "country" key is "USA" and the "population" key is greater than 1000000.

# Tips: Generate some random data in disc format -
[
    {'country': 'some country name', 'population': 'some population value'},
    {'country': 'some country name', 'population': 'some population value'}
]


starting_list = [
    {'country': 'USA', 'population': 10_000_000},
    {'country': 'USA', 'population': 100_000},
    {'country': 'Canada', 'population': 2_000_000}
]

new_list = []

for dictionary in starting_list:

    if dictionary['country'] == 'USA' and dictionary['population'] > 1_000_000:
        new_list.append(dictionary)

# ------------------------------------------------------------------------------------------------ #

        
# 3. Write a Python program that takes a dictionary as input and
# returns a new dictionary where the keys and values are swapped.

# Tips: Generate starting dictionaries by yourself.



starting_dictionary = {
    'name': 'Milan',
    'surname': 'Mitrovic'
}


new_dictionary = dict()

for key, value in starting_dictionary.items():
    new_dictionary[value] = key

# ------------------------------------------------------------------------------------------------ #

# 4. Write a Python program that takes a list of dictionaries and
# returns a new list containing only the dictionaries where the
# "name" key starts with the letter "J".

# Tips: Create your own starting list with dictionaries that
# will be used in this example.

starting_list_with_dictionaries = [
    {'name': 'Milan', 'surname': 'Mitrovic'},
    {'name': 'Jessica', 'surname': 'bla bla bla'}
]

new_list = []

for i in starting_list_with_dictionaries:
    if i['name'][0].lower() == 'j':
        new_list.append(i)
        
# ------------------------------------------------------------------------------------------------ #


# 5. Write a Python program that takes two dictionaries
# and merges them into a single dictionary.

dict_1 = {'name': 'wdd', 'surname': 'dwewwc'}

dict_2 = {'age': 22, 'country': 'Serbia'}

new_dict = dict_1.copy()

new_dict.update(dict_2)

new_dict

# ------------------------------------------------------------------------------------------------ #

# 6. Write a Python program that takes a list of dictionaries
# and returns a new list containing only the dictionaries where
# the "age" key is greater than or equal to 18.

# Tips: Generate your own list with dictionaries that
# will be used in this example.

starting_list_with_dictionaries = [

    {'name': 'edee', 'age': 20},
    {'name': 'dedw', 'age': 15}
]

new_list = []

for i in starting_list_with_dictionaries:
    if i['age'] > 18:
        new_list.append(i)

new_list

# ------------------------------------------------------------------------------------------------ #


# 7. Write a Python program that counts the frequency of
# each word in a string using a dictionary.

# Tips: Generate starting string/sentence by yourself.


my_string = 'Sto je danas lep i suncan1 dan. Sto je danas1 lep i suncan dan.'


my_dict = dict()

for word in my_string.split(' '):

    try:
        my_dict[word] = my_dict[word] + 1
    except KeyError:
        my_dict[word] = 1

my_dict

# ------------------------------------------------------------------------------------------------ #


# 8. Write a Python function that takes a dictionary as
# input and returns the keys in alphabetical order.

# Tips: Google solution for this example. We haven't covered
# all elements that will be needed for solution.


starting_dictionary = {

    'a': 1,
    'b': 2,
    'g': 9,
    'y': 10,
    'e': -8,
    'c': -2,
}

temporary_list = []

for key in starting_dictionary.keys():
    temporary_list.append(key)

temporary_list_sorted = sorted(temporary_list)

temporary_list_sorted

new_dict = dict()

for i in temporary_list_sorted:
    new_dict[i] = starting_dictionary[i]


new_dict

# ------------------------------------------------------------------------------------------------ #


# 9. Write a Python program that starts with a dictionary and
# returns a new dictionary containing only the key-value pairs
# where the value is an even number.

# Tips: Generate starting dictionary by yourself.


starting_dictionary = {
    'a': 1,
    'b': 2,
    'c': 13,
    'd': 14
}

new_dict = dict()


for key, value in starting_dictionary.items():

    if value % 2 == 0:
        new_dict[key] = value


new_dict

# ------------------------------------------------------------------------------------------------ #


# 10. Write a Python program that starts with list of dictionaries
# and a KEY and returns a new list containing only the
# dictionaries where the specified KEY is present.

# Tips: Generate starting list with dictionaries and KEY by
# yourself.


starting_list_with_dictionaries = [

    {
        'a': 1,
        'b': 2
    },

    {
        'c': 4,
        'd': 6
    },

    {
        'a': 7,
        'f': 9
    }

]


starting_key = 'a'

new_list = []


for i in starting_list_with_dictionaries:

    if starting_key in i.keys():

        new_list.append(i)


new_list

# ------------------------------------------------------------------------------------------------ #

# 11. Write a Python program that takes a dictionary and
# returns the sum of all the values in the dictionary.


starting_dictionary = {

    'a': 7,
    'b': 9,
    'c': 2
}


sum_ = 0


for value in starting_dictionary.values():
    sum_ = sum_ + value

sum_

# ------------------------------------------------------------------------------------------------ #


# 12. Write a Python program that takes a dictionary
# and returns the key that has the highest value.

starting_dictionary = {

    'a': 7,
    'b': 9,
    'c': 2
}

highest_value_so_far = 0
highest_key_so_far = ''

for k, v in starting_dictionary.items():

    if highest_value_so_far < v:
        # Set key to 'highest' key so far
        highest_key_so_far = k

        # Increase highest value so far
        highest_value_so_far = v


highest_key_so_far
highest_value_so_far

# ------------------------------------------------------------------------------------------------ #


# 13. Write a Python program that takes a dictionary
# and a list of keys as input and returns a new dictionary
# containing only the key-value pairs where the key is in
# the specified list.

# Tips: Generate data that should be used in this example.


starting_dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}

list_of_keys = ['a', 'd']


new_dictionary = dict()


for k, v in starting_dictionary.items():

    if k in list_of_keys:
        new_dictionary[k] = v


new_dictionary

# ------------------------------------------------------------------------------------------------ #


# 14. Write a Python program that takes a list of dictionaries
# and returns a new list containing only the dictionaries where
# the "name" key is present and the "age" key is less than 30.

# Tips: Generate data that should be used in this example.


starting_list_with_dictionaries = [

    {
        'name': 'dlnmd',
        'age': 20
    },

    {
        'name1': 'eddeqa',
        'age': 25
    },

    {
        'name': 'edwcd',
        'age': 35
    }
]

new_dictionary = dict()


for i in starting_list_with_dictionaries:

    if 'name' in i.keys() and i['age'] < 30:
        new_dictionary['name'] = i['name']
        new_dictionary['age'] = i['age']

[new_dictionary]

# ------------------------------------------------------------------------------------------------ #


# 15. Write a Python function that takes a dictionary and a
# value as input and returns a list of keys that have that value.

# Tips: Generate data that should be used in this example.


starting_dictionary = {
    'a': 1,
    'b': 4,
    'c': 1,
    'd': 7,
    'e': 1
}


starting_value = 1

new_list = []


for k, v in starting_dictionary.items():
    if v == starting_value:
        new_list.append(k)


new_list

# ------------------------------------------------------------------------------------------------ #



