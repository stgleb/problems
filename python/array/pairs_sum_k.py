"""
Found all possible index pairs Q and P
where A[Q] + A[P] == K for given K
"""


def get_pairs_count(K, A):
    A.sort()
    B = [A[0]]
    d = {}

    for v in A:
        if v in d:
            d[v] += 1
        else:
            d[v] = 1

    for i in range(len(A)):
        if A[i] == B[len(B) - 1]:
            continue
        else:
            B.append(A[i])

    A = B
    left = 0
    right = len(A) - 1
    count = 0

    while left <= right:
        if A[left] + A[right] == K:
            if left != right:
                count += d[A[left]] * d[A[right]] * 2
            else:
                count += d[A[left]] * d[A[right]]
            left += 1
            right -= 1
        elif A[left] + A[right] > K:
            right -= 1
        elif A[left] + A[right] < K:
            left += 1

    return count


def get_pairs_count2(K, A):
    d = dict()
    count = 0

    for val in A:
        if val in d:
            d[val] += 1
        else:
            d[val] = 1

    for val in A:
        tmp = K - val

        if tmp in d:
            first = d[tmp]
            second = d[val]

            if tmp != val:
                count += first * second * 2
            else:
                count += 1
            d[val] = 0

    return count


if __name__ == "__main__":
    A = [1, 8, -3, 0, 1, 3, -2, 4, 5]
    print(get_pairs_count(6, A))
    print(get_pairs_count2(6, A))
    # A = [1, 1, 1]
    # print(solution(A, 2))
