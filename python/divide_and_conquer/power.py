"""
Calculate power x^n in O(logN)
"""


def qpow(a, n):
    tmp = 1

    while n:
        if n & 1:
            tmp *= a
            n -= 1
        else:
            a *= a
            n >>= 1

    return tmp


if __name__ == "__main__":
    print(qpow(2, 4))
    print(qpow(3, 5))
    print(qpow(2, 8))
    print(qpow(2, 64))
