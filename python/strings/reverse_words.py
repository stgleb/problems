"""
Given a text, reverse characters in words.
"""


def is_letter(c):
    return (ord(c) >= ord('A') and ord(c) <= ord('Z')) or \
           (ord(c) >= ord('a') and ord(c) <= ord('z'))


def reverse(text):
    result = []
    stack = []

    for i in range(len(text)):
        if not is_letter(text[i]):
            if stack:
                result += stack[::-1]
                stack = []
            result.append(text[i])
        else:
            stack.append(text[i])

    if stack:
        result += stack[::-1]

    return ''.join(result)


if __name__ == "__main__":
    s = "Example text to reverse"
    print(reverse(s))
