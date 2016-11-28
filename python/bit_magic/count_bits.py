"""
Count positive bits in integer
"""


def count(n):
    cnt = 0

    while n:
        n &= n-1
        cnt += 1

    return cnt


if __name__ == "__main__":
    print(count(7))
    print(count(17))
    print(count(5))
