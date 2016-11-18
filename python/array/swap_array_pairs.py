"""
There are n-pairs and therefore 2n people. everyone has one unique number
ranging from 1 to 2n. All these 2n persons are arranged in random fashion
in an Array of size 2n. We are also given who is partner of whom.
Find the minimum number of swaps required to arrange these pairs
such that all pairs become adjacent to each other.

    Input:
    n = 3
    pairs[] = {1->3, 2->6, 4->5}  // 1 is partner of 3 and so on
    arr[] = {3, 5, 6, 4, 1, 2}

    Output: 2
    We can get {3, 1, 5, 4, 6, 2} by swapping 5 & 6, and 6 & 1
"""


def arrange(arr, pairs):
    if len(arr) < 2:
        return 0
    elif pairs[arr[0]] == arr[1]:
        # If first two elements are already paired
        return arrange(arr[2:], pairs)
    else:
        index = 0

        # Find position of paired element in the array
        while index < len(arr) and arr[index] != pairs[arr[0]]:
            index += 1

        arr1 = arr[:]
        arr2 = arr[:]

        # Swap first element with second
        arr1[1], arr1[index] = arr1[index], arr1[1]
        result1 = arrange(arr1[2:], pairs)
        # Swap in another way and compare results
        arr2[0], arr2[index - 1] = arr2[index - 1], arr2[0]
        result2 = arrange(arr2[2:], pairs)

        return min(result1, result2) + 1


if __name__ == "__main__":
    arr = [3, 5, 6, 4, 1, 2]
    pairs = {1: 3, 2: 6, 4: 5,
             3: 1, 6: 2, 5: 4}

    print(arrange(arr, pairs))
