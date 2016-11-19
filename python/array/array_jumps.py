"""
    Non empty array A is given
    Pawn is placed on zero index A[0]
    Pawn can move to the next index next = current + A[current]
    Print number of moves pawn need to do to escape from an array
    of -1 if it is impossible
"""


def get_jumps_count(A):
    escapable = False
    position = 0
    count = 0

    for i in range(len(A)):
        if A[i] + i > len(A) - 1 or A[i] + i < 0:
            escapable = True
            break

    if not escapable:
        return -1

    while True:
        if position >= len(A) or position < 0:
            return count

        if A[position] is None:
            return -1

        count += 1
        step = A[position]
        A[position] = None
        position = step + position

    return count


if __name__ == '__main__':
    A = [1, 1, -1, 1]
    print(get_jumps_count(A))
