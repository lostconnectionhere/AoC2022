# with open('AoC_input_day3.txt','r') as f:
#     data = f.read().splitlines()

#test data
data = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg','wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']

#split string in half
s = "vJrwpWtwJgWrhcsFMMfFFhFp"
part1 = s[:len(s)//2]
part2 = s[len(s)//2:]
print("The first part of string: ", part1)
print("The second part of string: ", part2)

#find same character
for char in part1:
    for char2 in part2:
        if char == char2:
            print('zelfde character: ', char2)

#give value to lowercase letter
import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1

print(values[char2])

#give value to uppercase letter
values_capital = dict()
for index, letter in enumerate(string.ascii_uppercase):
    values_capital[letter] = index + 27

print(values_capital['Z'])
