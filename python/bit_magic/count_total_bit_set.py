"""
Given a number - n, count all set bits in numbers between 1 and n
"""


def leftmost_bit_set(n):
    m = 0

    while n > 1:
        n >>= 1
        m += 1

    return m


def next_leftmost_bit_set(n, m):
    temp = 1 << m

    while n < temp:
        temp >>= 1
        m -= 1

    return m


def count_bit_util(n, m):
    if n == 0:
        return 0

    m = next_leftmost_bit_set(n, m)

    if n == (1 << (m + 1)) - 1:
        return (m + 1) * (1 << m)

    # Set leftmost bit to 0
    n -= (1 << m)
    return (n + 1) + count_bit(n) + m * (1 << (m - 1))


def count_bit(n):
    m = leftmost_bit_set(n)
    return count_bit_util(n, m)


if __name__ == "__main__":
    print(count_bit(7))
