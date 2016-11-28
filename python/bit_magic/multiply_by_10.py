"""
Write a function to multiply number on 10, without using multiplication
operator
"""


def multiply(n):
    """
    Simple trick n * 2 + n * 8
    :param n:
    :return:
    """
    return (n << 1) + (n << 3)


if __name__ == "__main__":
    print(multiply(8))
    print(multiply(43))
