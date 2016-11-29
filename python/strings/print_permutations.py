"""
Print all permutations of given string
"""


def permute(s, l, r, result):
    if l == r:
        result.append(s[:])
    else:
        for i in range(l, r):
            s[l], s[i] = s[i], s[l]
            permute(s, l + 1, r, result)
            s[l], s[i] = s[i], s[l]


def permutations(s):
    result = []
    permute(list(s), 0, len(s), result)

    return result


if __name__ == "__main__":
    s = "cat"
    print(permutations(s))
