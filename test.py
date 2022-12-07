with open('AoC_input_day3.txt','r') as f:
    data = f.read().splitlines()
    
data = [['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'],['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']]

split_data = [i for i in range(0, len(data), 3)]

parts = [data[ind:ind + 3] for ind in split_data]

# print(parts)

letter = ''
item_list_lower = []
item_list_upper = []


for subset1 in parts:  
    # print(subset1) # prints the entire list with the sublists
    for subset2 in subset1:
        # print(subset2) # prints the sublists separately
        for subset3 in subset2:
            # print(subset3) # prints the separate strings per sublist
            #find same character per sublist
            for character in subset3[0]:
                print(character)
                # for character2 in subset3[1]:
                #     if character == character2:
                #         for character3 in subset3[2]:
                #             if character == character3:
                #                 letter = character 
                #                 print(letter)      
                #         break
print(letter)