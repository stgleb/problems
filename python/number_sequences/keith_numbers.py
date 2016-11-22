"""
A n digit number x is called Keith number if it appears in a special sequence (defined below)
generated using its digits. The special sequence has first n terms as digits of x and other
terms are recursively evaluated as sum of previous n terms.

Input : x = 197
Output : Yes
197 has 3 digits, so n = 3
The number is Keith because it appears in the special
sequence that has first three terms as 1, 9, 7 and
remaining terms evaluated using sum of previous 3 terms.
1, 9, 7, 17, 33, 57, 107, 197, .....
"""


def is_keith_number(n):
    visited = set()
    digits = map(int, list(str(n)))
    next = 0

    while next < n:
        next = sum(digits[-3:])

        if next in visited:
            return False

        visited.add(next)

        if next == n:
            return True

        digits = digits[-2:]
        digits.append(next)

    return False


if __name__ == "__main__":
    N = 197
    print(is_keith_number(N))
    N = 24
    print(is_keith_number(N))
