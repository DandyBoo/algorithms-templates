def combinations(input_string):
    keyboard = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    if input_string == '':
        return ['']

    data = []
    letters = keyboard[input_string[-1]]

    for combination in combinations(input_string[:-1]):
        for letter in letters:
            data.append(combination + letter)

    return data


print(' '.join(combinations(input())))
