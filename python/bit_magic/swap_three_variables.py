"""
Swap three variables a,b,c without using temporary variable

1, 2, 3 -> 3, 1, 2
"""


def swap_arithm(a, b, c):
    a = a + b + c
    b = a - b - c
    c = a - b - c
    a = a - b - c

    return a, b, c


def swap_bin(a, b, c):
    a = a ^ b ^ c
    b = a ^ b ^ c
    c = a ^ b ^ c
    a = a ^ b ^ c

    return a, b, c


if __name__ == "__main__":
    print(swap_arithm(1, 2, 3))
    print(swap_bin(1, 2, 3))
