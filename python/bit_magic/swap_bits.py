"""
Swap even and odd bits

 1011 -> 0111

"""


def swap_bits(n):
    return ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)


if __name__ == "__main__":
    print(swap_bits(10))
