"""
Check whether sting is rotation of another
"""


def is_rotation(s1, s2):
    s1s1 = s1 + s1

    return s1s1.find(s2) != -1


if __name__ == "__main__":
    s1 = "waterbootle"
    s2 = "ootlewaterb"
    print(is_rotation(s1, s2))
