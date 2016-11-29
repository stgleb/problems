"""
Given a string, find first non-repeating character
"""


def find_firts_non_repeating_chart(s):
    d = {}

    for i in range(len(s)):
        if s[i] in d:
            return d[s[i]]
        else:
            d[s[i]] = i

    return None


if __name__ == "__main__":
    s = "dample g string"
    print(find_firts_non_repeating_chart(s))

