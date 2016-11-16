"""
Find longest common substring of two strings
"""


def lcs_naive(s1, s2):
    """
    Naive O(N^3) solution
    :param s1:
    :param s2:
    :return:
    """
    max_len = 0
    pos1, pos2 = 0, 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            count = 0
            k, l = i, j

            while k < len(s1) and l < len(s2) and s1[k] == s2[l]:
                k += 1
                l += 1
                count += 1

            if count > max_len:
                max_len = count
                pos1 = i
                pos2 = j

    return pos1, pos2, max_len


def lcs_dynamic(s1, s2):
    """
    Dynamic programming based solution O(N^2) complexity
    :param s1:
    :param s2:
    :return:
    """
    lcs = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
    result = 0
    x, y = 0, 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1

                if result < lcs[i][j]:
                    result = lcs[i][j]
                    x = i - lcs[i][j] + 1
                    y = j - lcs[i][j] + 1

    return x, y, result


if __name__ == "__main__":
    s1 = "GeeksforGeeksQ"
    s2 = "GeeksQuiz"
    print(lcs_naive(s1, s2))
    print(lcs_dynamic(s1, s2))
