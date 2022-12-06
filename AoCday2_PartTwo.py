with open('AoC_input_day2.txt','r') as f:
    data = f.read().splitlines()

# data = ['A Y', 'B X', 'C Z'] #test

score = 0
for i in data:
    if i == 'A X':
        score += 3
        print('Score: ', score)
    elif i == 'A Y':
        score += 4
        print('Score: ', score)
    elif i == 'A Z':
        score += 8
        print('Score: ', score)
    elif i == 'B X':
        score += 1
        print('Score: ', score)
    elif i == 'B Y':
        score += 5
        print('Score: ', score)
    elif i == 'B Z':
        score += 9
        print('Score: ', score)
    elif i == 'C X':
        score += 2
        print('Score: ', score)
    elif i == 'C Y':
        score += 6
        print('Score: ', score)
    elif i == 'C Z':
        score += 7
        print('Score: ', score)

print('Total score: ', score)

