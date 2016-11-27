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
    """
    If number n is power of 2  - 1 - return answer,
    otherwise count number of set bits when m bit is 1,
    and call recursive for count bits when m bit is 0.
    :param n:
    :param m:
    :return:
    """
    if n == 0:
        return 0

    m = next_leftmost_bit_set(n, m)

    if n == (1 << (m + 1)) - 1:
        return (m + 1) * (1 << m)

    # Set leftmost bit to 0
    n -= (1 << m)
    return (n + 1) + count_bit(n) + m * (1 << (m - 1))


def count_bit(n):
    """
    Solution with O(LogN) time complexity, based on rule that
    count if set bits for [2^n, 2^(n - 1)) is n * 2 ^(n - 1).
    :param n:
    :return:
    """
    m = leftmost_bit_set(n)
    return count_bit_util(n, m)


def count_bit_set_naive_util(n):
    cnt = 0

    while n:
        cnt += n & 1
        n >>= 1

    return cnt


def count_bit_set_naive(n):
    """
    Naive O(N) solution
    :param n:
    :return:
    """
    cnt = 0

    for i in range(1, n + 1):
        cnt += count_bit_set_naive_util(i)

    return cnt


if __name__ == "__main__":
    print(count_bit(7))
    print(count_bit_set_naive(7))
