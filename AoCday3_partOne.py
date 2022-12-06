with open('AoC_input_day3.txt','r') as f:
    data = f.read().splitlines()

#test data
# data = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg','wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']

item_list_lower = []
item_list_upper = []

for string in data:
    part1 = string[:len(string)//2]
    part2 = string[len(string)//2:]
    # print("The first part of string: ", part1)
    # print("The second part of string: ", part2)
    #find same character
    for character in part1:
        for character2 in part2:
            if character == character2:
                letter = character          
                break

    # print("Item found in both compartments are: ", letter)
    # item_list += letter

    if letter.isupper() == False:
        item_list_lower += letter
        # print('Letter', letter, 'is in lowercase')
    else:
        item_list_upper += letter
        # print('Letter', letter, 'is in uppercase')

# print(item_list_lower)
# print(item_list_upper)

import string
values = dict()

# total score for lowercase items
total_count_lower = 0
for item in item_list_lower:
    for index, letter in enumerate(string.ascii_lowercase):
        values[letter] = index + 1
    total_count_lower += (values[item])
    # print(item)
    # print(values[item])

# print('Total score for lowercase items are: ', total_count_lower)

# total score for lowercase items
total_count_upper = 0
for item in item_list_upper:
    for index, letter in enumerate(string.ascii_uppercase):
        values[letter] = index + 27
    total_count_upper += (values[item])
    # print(item)
    # print(values[item])

# print('Total score for uppercase items are: ', total_count_upper)

total = total_count_lower + total_count_upper 

print('Total score of items are: ', total)
