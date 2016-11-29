"""
Given a string, remove all duplicates from it preserving original order
of characters
"""


def remove_duplicates(s):
    d = {}
    result = []

    for c in s:
        if c not in d:
            result.append(c)
            d[c] = True

    return ''.join(result)


if __name__ == "__main__":
    s = "geeksforgeeks"
    print(remove_duplicates(s))
