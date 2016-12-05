"""
Z function of string s ia and array z, where z[i] value is amount of numbers
from ith position in string s which are the same with first z[i] characters of
string s
"""


def z_function_naive(s):
    z = [0 for _ in range(len(s))]

    for i in range(1, len(s)):
        j = 0
        k = i

        while k < len(s) and s[j] == s[k]:
            j += 1
            k += 1

        z[i] = j

    return z


def z_function(s):
    l, r = 0, 0
    z = [0 for _ in range(len(s))]

    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])

        while i + z[i] < len(s) and s[z[i]] == s[z[i] + i]:
            z[i] += 1

        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    return z


if __name__ == "__main__":
    s = "abacaba"
    print(z_function_naive(s))
    print(z_function(s))
