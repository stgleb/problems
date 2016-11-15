"""
Given a string, substitute all whitespaces with %20 in place,
for simplicity, use list and assume at the end there is enough free
space.
"""


def subsitute(l, n):
    j = len(l) - 1

    for i in range(n - 1, -1, -1):
        if l[i] == ' ':
            l[j] = '0'
            l[j - 1] = '2'
            l[j - 2] = '%'
            j -= 3
        else:
            l[j] = l[i]
            j -= 1

    return l

if __name__ == "__main__":
    s = "hello beautiful world!!!"
    l = list(s)
    length = len(l)
    l.append('')
    l.append('')
    l.append('')
    l.append('')
    print(subsitute(l, length))
