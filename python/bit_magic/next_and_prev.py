"""
Given a number, return two numbers with the same count of 1 bits
closest from  up and down
"""


def first_positive(n, i=0):
    while 1 << i & n == 0 and 1 << i < n:
        i += 1

    return i


def first_negative(n, i=0):
    while 1 << i & n and 1 << i < n:
        i += 1

    return i


def get_closest_numbers(n):
    lower = n
    upper = n

    i = first_negative(n)
    lower |= 1 << i
    i = first_positive(lower, i + 1)
    lower ^= 1 << i

    i = first_positive(n)
    upper ^= 1 << i
    i = first_negative(upper, i + 1)
    upper |= 1 << i

    return lower, upper


if __name__ == "__main__":
    print(get_closest_numbers(5))
    print(get_closest_numbers(10))
