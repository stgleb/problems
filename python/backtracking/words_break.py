"""
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "sampleteststring",
dict = ["sample", "test", "word", "string", "test"]
"""


def word_break(s, d, breaks, cur=""):
    if not s:
        breaks.add(cur)
        return

    for i in range(len(s) + 1):
        if s[:i] in d:
            word_break(s[i:], d, breaks, cur + " " + s[:i])


if __name__ == "__main__":
    s = "sampleteststring"
    d = {"sample", "test", "word", "string", "test", "te", "st"}
    result = set()
    word_break(s, d, result)
    print(result)
