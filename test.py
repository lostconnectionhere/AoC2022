with open('AoC_input_day3.txt','r') as f:
    data = f.read().splitlines()
    
# data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""


#input
list1 = ['x','y','z','a','b','c','d','e','f','g']

split_points = [i for i in range(0, len(data), 3)]

parts = [data[ind:ind + 3] for ind in split_points]

print(parts)
