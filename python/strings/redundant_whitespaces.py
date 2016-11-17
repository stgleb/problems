"""
Remove redundant whitespaces from string
"""


def remove_whitespaces(lst):
    i, j = 0, 0

    while j < len(lst):
        if lst[j] != ' ':
            lst[i] = lst[j]
            i += 1
            j += 1
        else:
            lst[i] = lst[j]
            i += 1
            j += 1

            while lst[j] == ' ':
                j += 1

    return ''.join(lst[:i])


if __name__ == "__main__":
    s = "hello  I    am computer"
    l = list(s)
    print(remove_whitespaces(l))
