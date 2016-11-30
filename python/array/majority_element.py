"""
Majority Element: A majority element in an array A[] of size n is an element
that appears more than n/2 times (and hence there is at most one such element).

Write a function which takes an array and emits the majority element (if it exists),
otherwise prints NONE as follows
"""


def find_majority_element(arr):
    maj_index = 0
    count = 0

    for i in range(1, len(arr)):
        if arr[i] == arr[maj_index]:
            count += 1
        else:
            count -= 1

        if count == 0:
            maj_index = i
            count = 1

    return arr[maj_index]


if __name__ == "__main__":
    arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    print(find_majority_element(arr))
