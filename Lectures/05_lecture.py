

import pandas as pd

df = pd.read_csv('moji_podaci.csv', delimiter=', ', engine='python')

df

moji_podaci = open('moji_podaci.csv')


moji_podaci


def read_csv_file(path):
    """
    Purpose of this function is to
    read file.

    :param path:
    :type path:
    :return: List with data.
    :rtype:
    """

    my_file = open(path)

    list_sa_podacima = []

    for red_u_fajlu_sa_podacima in my_file:
        list_sa_podacima.append(red_u_fajlu_sa_podacima)

    return list_sa_podacima


def clean_my_data(list_):
    processed_list = []

    for i in list_:
        processed_list.append(i.replace('\n', ''))

    return processed_list


def create_list_from_strings_elements(list_: list) -> list:
    """
    Purpose of this function is ...

    :param list_:
    :type list_:
    :return:
    :rtype:
    """

    processed_list = []

    for i in list_:
        processed_list.append(i.split(', '))

    return processed_list


def add_last_two_sublists(first_list, second_list):

    list_wit_totals = []
    for x, y in zip(first_list, second_list):
        list_wit_totals.append(int(x) + int(y))

    return list_wit_totals


first_list = read_csv_file(path='moji_podaci.csv')

first_list

second_list = clean_my_data(list_=first_list)

second_list


third_list = create_list_from_strings_elements(list_=second_list)

third_list


fourth_list = add_last_two_sublists(first_list=third_list[-1], second_list=third_list[-2])

fourth_list


def write_data_to_file(
        data,
        path
):
    with open(f'{path}', mode='w') as f:
    
        f.write(data.__str__())


write_data_to_file(data=fourth_list, path='moj_novi_fijl.csv')

