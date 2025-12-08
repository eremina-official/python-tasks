# Exercise for input, dictionaries

numbersMapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
}

userInput = input('Please enter number: ')
result = ''

for item in userInput:
    # result = result + numbersMapping[item] + ' '
    result += numbersMapping.get(item, '!') + ' '

print(f'Result is: {result}')

