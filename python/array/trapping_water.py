"""
Given n non-negative integers representing an elevation map where
the width of each bar is 1, compute how much water it is able to
trap after raining.
"""


def trapping_water(a):
    left, right = 0, len(a) - 1
    left_max = a[left]
    right_max = a[right]
    count = 0

    while left < right:
        # Compare max from left side to max from right side
        # Move forward pointer from the side where min of two max
        if left_max < right_max:
            count += left_max - a[left]
            left += 1

            # Try to update new max on left side
            if a[left] > left_max:
                left_max = a[left]
        else:
            count += right_max - a[right]
            right -= 1

            # Try to update max on right side
            if a[right] > right_max:
                right_max = a[right]

    return count


if __name__ == "__main__":
    # 2 + 1 + 3 + 1 + 1 = 8
    a = [3, 1, 2, 0, 4, 1, 1, 2]
    print(trapping_water(a))
