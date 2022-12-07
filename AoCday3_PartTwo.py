# test data

data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

data = data.splitlines()
print(type(data))

# letter = ''

item_list_lower = []
item_list_upper = []
x = 0
y = 1
z = 2

for string in data:
    first_elf = data[x]
    second_elf = data[y]
    third_elf = data[z]
    #find same character
    for character in first_elf:
        for character2 in second_elf:
            if character == character2:
                for character3 in third_elf:
                    if character == character3:
                        letter = character       
                break
    x += 3
    y += 3
    z += 3

print(letter)

if letter.isupper() == False:
    item_list_lower += letter
    print('Letter', letter, 'is in lowercase')
else:
    item_list_upper += letter
    print('Letter', letter, 'is in uppercase')

print(item_list_lower)
print(item_list_upper)

