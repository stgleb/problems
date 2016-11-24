"""
Given a string s and a dictionary of words dict, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "sampleteststring",
dict = ["sample", "test", "word", "string", "test"]
"""


def word_break(s, d, breaks, cur=""):
    """
    Recursive solution
    :param s: original text
    :param d: dictionary
    :param breaks: set to handler the result
    :param cur: current split of text
    :return:
    """
    if not s:
        breaks.add(cur)
        return

    for i in range(len(s) + 1):
        if s[:i] in d:
            word_break(s[i:], d, breaks, cur + " " + s[:i])


def word_break_iteratively(s, d):
    """
    Iterative solution using stack

    :param s: original text
    :param d: dictionary of words
    :return:
    """
    stack = [[s, []]]
    result = []

    while stack:
        text, breaks = stack.pop()

        if not text:
            result.append(breaks)
            continue

        for i in range(len(text) + 1):
            if text[:i] in d:
                stack.append([text[i:], breaks + [text[:i]]])

    return result


if __name__ == "__main__":
    s = "sampleteststring"
    d = {"sample", "test", "word", "string", "test", "te", "st"}
    result = set()
    word_break(s, d, result)
    print(result)
    print(word_break_iteratively(s, d))
