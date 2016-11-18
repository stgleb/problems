"""
List of prices on stock market is given,
find two days for buy and sell stock to get
maximum profit.
"""


def max_profit(arr):
    min_index = 0
    profit = 0
    begin, end = 0, 0

    for i in range(len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i

        diff = arr[i] - arr[min_index]

        if diff > profit:
            profit = diff
            begin = min_index
            end = i

    return begin, end


if __name__ == "__main__":
    arr = [7, 8, 1, 4, 5, 3, 6]
    print(max_profit(arr))
