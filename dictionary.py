'''
Gloria Pappalardo
October 2, 2020
Python 3.8
This script creates a dictionary holding information about the populations of refugee camps in Bangladesh, India, Jordan, Botswana, and Liberia in 2014. 
It iterates through the dictionary and outputs information. Then it prints the country names, the populations of refugees, and statements about 
the number of refugees in each country.
'''
# refugee_dict is assigned the dictionary with refugee population information for several countries
refugee_dict = {'Bangladesh': 32355, 'India': 65057, 'Jordan': 96088, 'Botswana': 2833, 'Liberia': 29028}
# print(refugee_dict)

# this function prints out just the country names from the dictionary by looping through the keys of the dictionary
# and using the .keys() method
def print_country(dict):
    for x in dict.keys():
        print(x)
# print_country(refugee_dict)

# this function prints out just the populations of refugees by looping through the values of the dictionary
# and using the .values() method
def print_population(dict):
    for x in dict.values():
        print(x)
# print_population(refugee_dict)

# I created a function, print_countrypop, that takes the input of a dictionary and prints out the keys and
# the values as part of sentences that describe the refugee populations in each country. This function uses the .items()
# method and string concatenation
def print_countrypop(dict):
    for (x, y) in dict.items():
        print(x + ' has ' + str(y) + ' refugees.')

# print_countrypop(refugee_dict)
