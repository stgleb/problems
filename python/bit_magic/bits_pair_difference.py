"""
Given an integer array of n integers, find sum of bit differences in all
pairs that can be formed from array elements. Bit difference of a pair (x, y)
is count of different bits at same positions in binary representations of x and y.
For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7
is 111 ( first and last bits differ in two numbers).

Input: arr[] = {1, 2}
Output: 4
All pairs in array are (1, 1), (1, 2)
                       (2, 1), (2, 2)
Sum of bit differences = 0 + 2 +
                         2 + 0
                      = 4

Input:  arr[] = {1, 3, 5}
Output: 8
All pairs in array are (1, 1), (1, 3), (1, 5)
                       (3, 1), (3, 3) (3, 5),
                       (5, 1), (5, 3), (5, 5)
Sum of bit differences =  0 + 1 + 1 +
                          1 + 0 + 2 +
                          1 + 2 + 0
                       = 8
"""


def difference_bit_count(arr):
    """
    Program assumes that integers are 32 bit

    :param arr: array of integers
    :return:
    """
    n = len(arr)
    mask = 1
    result = 0

    for i in range(32):
        count = 0

        for v in arr:
            if v & (mask << i):
                count += 1

        result += count * (n - count) * 2

    return result


if __name__ == "__main__":
    print(difference_bit_count([1, 3, 5]))
    print(difference_bit_count([1, 2]))
