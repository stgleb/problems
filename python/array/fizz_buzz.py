"""
Write a program that prints the numbers from 1 to 100. But for multiples of three print
Fizz instead of the number and for the multiples of five print Buzz. For numbers which
 are multiples of both three and five print FizzBuzz.
"""


def fizz_buzz(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fizz_buzz2(n):
    strs = ["" for _ in range(n + 1)]

    for i in range(0, n + 1, 3):
        strs[i] += "Fizz"

    for i in range(0, n + 1, 5):
        strs[i] += "Buzz"

    for i in range(n + 1):
        print("{0} {1}".format(i, strs[i]))


if __name__ == "__main__":
    # fizz_buzz(100)
    fizz_buzz2(100)
