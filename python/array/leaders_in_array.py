"""
Write a program to print all the LEADERS in the array. An element is leader
if it is greater than all the elements to its right side. And the rightmost
element is always a leader. For example int the array {16, 17, 4, 3, 5, 2},
leaders are 17, 5 and 2.
"""


def find_leaders(arr):
    cur_max = 0
    leaders = []

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > cur_max:
            cur_max = arr[i]
            leaders.append(arr[i])

    return leaders[::-1]


if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    print(find_leaders(arr))
