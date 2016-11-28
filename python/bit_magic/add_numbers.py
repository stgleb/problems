"""
Add two numbers without using arithmetic operations
"""


def add(a, b):
    while b:
        tmp = a & b
        a = a ^ b
        b = tmp << 1

    return a


if __name__ == "__main__":
    print(add(3, 5))
    print(add(2, 4))
