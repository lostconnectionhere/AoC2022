with open('AoC_input_day3.txt','r') as f:
    data = f.read().splitlines()

#test data
# data = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg','wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']

item_list = []
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
    item_list += letter

    if letter.isupper() == False:
        print('Letter', letter, 'is in lowercase')
    else:
        print('Letter', letter, 'is in uppercase')

print(item_list)


# letter = "B"

# if letter.isupper() == False:
# 	print('Letter is lowercase: ', letter)
# else:
# 	print('Letter is lowercase: ', letter, 'is not lowercase')


# import string
# values = dict()

# for index, letter in enumerate(string.ascii_lowercase):
#     values[letter] = index + 1

# print(values['p'])


    # #give value to lowercase letter
    # import string
    # values = dict()
    # for index, letter in enumerate(string.ascii_lowercase):
    #     values[letter] = index + 1

    # print(values[character2])

    # #give value to uppercase letter
    # values_capital = dict()
    # for index, letter in enumerate(string.ascii_uppercase):
    #     values_capital[letter] = index + 27

    # print(values_capital[character2])



            





#give value to lowercase letter
# import string
# values = dict()
# for index, letter in enumerate(string.ascii_lowercase):
#     values[letter] = index + 1

# print(values[char2])

#give value to uppercase letter
# values_capital = dict()
# for index, letter in enumerate(string.ascii_uppercase):
#     values_capital[letter] = index + 27

# print(values_capital['Z'])
