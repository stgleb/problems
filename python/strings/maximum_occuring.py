"""
Given a string, return maximum occurring character within string
"""


def find_max_occuring(s):
    d = {}
    max_occur = s[0]

    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

        if d[c] > d[max_occur]:
            max_occur = c

    return max_occur


if __name__ == "__main__":
    s = "test"
    print(find_max_occuring(s))
