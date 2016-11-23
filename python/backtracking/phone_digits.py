"""
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters like on mobile phone.

    {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', '0'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }
"""


def get_combinations(keyboard, line, result, current=""):
    if not line:
        result.append(current)
        return

    digit = int(line[0])

    for letter in keyboard[digit]:
        get_combinations(keyboard, line[1:], result, current + letter)


def get_combinations_iterative(keyboard, line):
    combinations = ['']

    for digit in map(int, list(line)):
        tmp = []

        for letter in keyboard[digit]:
            for comb in combinations:
                tmp.append(comb + letter)

        combinations = tmp

    return combinations


if __name__ == "__main__":
    line = "273"
    result = []

    keyboard = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', '0'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

    get_combinations(keyboard, line, result)
    print(result)
    print(get_combinations_iterative(keyboard, line))
