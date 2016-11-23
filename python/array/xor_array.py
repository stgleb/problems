"""
Given an array of positive integers and a number x, find the number of pairs
of integers in the array whose XOR is equal to x.
"""


def find_pairs(a, X):
    d = {a[i]: i for i in range(len(a))}
    pairs = set()

    for i in range(len(a)):
        if a[i] ^ X in d:
            j = d[a[i] ^ X]
            t = tuple(sorted((i, j)))
            pairs.add(t)

    return list(pairs)


if __name__ == "__main__":
    a = [5, 4, 10, 15, 7, 6]
    print(find_pairs(a, 5))
