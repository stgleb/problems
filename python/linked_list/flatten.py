"""
Make nested list flat
"""


def flatten(arr):
    result = []

    for x in arr:
        if type(x) == list:
            result += flatten(x)
        else:
            result.append(x)

    return result


if __name__ == "__main__":
    print(flatten([1, 2, [3, [10, 20], 4], 5]))
