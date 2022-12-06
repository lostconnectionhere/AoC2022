# with open('AoC_input_day2.txt','r') as f:
#     data = f.read().splitlines()

data = ['A Y', 'B X', 'C Z'] #test

for i in data:
    if i == 'A X':
        print('Score: 4')
    elif i == 'A Y':
        print('Score: 8')
    elif i == 'A Z':
        print('Score: 3')
    elif i == 'B X':
        print('Score: 1')
    elif i == 'B Y':
        print('Score: 5')
    elif i == 'B Z':
        print('Score: 9')
    elif i == 'C X':
        print('Score: 7')
    elif i == 'C Y':
        print('Score: 2')
    elif i == 'C Z':
        print('Score: 6')

