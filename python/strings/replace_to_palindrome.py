"""
Given a string which has some lowercase alphabet characters and one special character dot(.).
We need to replace all dots with some alphabet character in such a way that resultant string
becomes a palindrome, in case of many possible replacements, we need to choose palindrome
string which is lexicographically smallest.  If it is not possible to convert string into
palindrome after all possible replacements then output Not possible.
"""


def replace(s):
    left, right = 0, len(s) - 1
    l = list(s)

    while left < right:
        if l[left] == l[right] == '.':
            l[left] = 'a'
            l[right] = 'a'
        elif l[left] == '.' or l[right] == '.':
            if l[right] == '.':
                l[right] = l[left]
            else:
                l[left] = l[right]
        elif l[left] != l[right]:
            return None

        left += 1
        right -= 1

    return ''.join(l)


if __name__ == "__main__":
    s = "ab..e.c.a"
    print(replace(s))
