with open('AoC_input_day1.txt','r') as openf:
    data = openf.read()

data = data.split('\n')

total = 0
max = 0
list_of_sums = []

for i in data:
    if i == "":
        list_of_sums.append(total)
        total = 0
    else:
        total += int(i)
        if total > max:
            max = total
            # print(max)
        else: 
            continue
# print(max)
list_of_sums.sort()

top_three = list_of_sums[-3] + list_of_sums[-2]  + list_of_sums[-1]
print(top_three)
