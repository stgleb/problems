"""
Print reverse of string recursive
"""


def print_reverse(s):
    if s:
        print_reverse(s[1:])
        print(s[0])


if __name__ == "__main__":
    print_reverse("hello")
