# test data

data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg """
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""

data = data.splitlines()
print(type(data))

# letter = ''

item_list_lower = []
item_list_upper = []


for string in data:
    #find same character
    for character in data[0]:
        for character2 in data[1]:
            if character == character2:
                for character3 in data[2]:
                    if character == character3:
                        letter = character       
                break

print(letter)

if letter.isupper() == False:
    item_list_lower += letter
    print('Letter', letter, 'is in lowercase')
else:
    item_list_upper += letter
    print('Letter', letter, 'is in uppercase')

print(item_list_lower)
print(item_list_upper)