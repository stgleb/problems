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


def trapping_rain_water_precomputed(a):
    left_max = [0 for _ in range(len(a))]
    right_max = [0 for _ in range(len(a))]
    water = 0
    left_max[0] = a[0]

    for i in range(1, len(a)):
        left_max[i] = max(a[i], left_max[i - 1])

    right_max[-1] = a[-1]
    for i in range(len(a) - 2, -1, -1):
        right_max[i] = max(a[i], right_max[i + 1])

    for i in range(len(a)):
        water += min(left_max[i], right_max[i]) - a[i]

    return water

if __name__ == "__main__":
    # 2 + 1 + 3 + 1 + 1 = 8
    a = [3, 1, 2, 0, 4, 1, 1, 2]
    print(trapping_water(a))
    print(trapping_rain_water_precomputed(a))
