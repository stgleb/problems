"""
Sort array of numbers of length n in O(N)
"""


def get_digit(number, i):
    """
    Return i-th digit from right side
    :param number:
    :param i:
    :return:
    """
    s = str(number)
    digit = int(s[len(s) - i - 1])

    return digit


def radix_sort(a, n):
    for i in range(n):
        d = {i: [] for i in range(10)}

        for v in a:
            digit = get_digit(v, i)
            d[digit].append(v)

        a = []

        for i in range(10):
            a += d[i]

    return a


if __name__ == "__main__":
    a = [134, 543, 358, 968, 769, 324, 656, 787, 345]
    print(radix_sort(a, 3))
