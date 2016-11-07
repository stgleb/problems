"""
    The text is given. Each word of this text is scrambled(letters are permuted)
    Whitespaces are removed. The problem is to restore original text from scrambled
    if dictionary of words is given.

    Input:
        dict: {"world", "hello", "apple", "pear"}
        text: "ehlololwrd"
    Output:
        hello world
"""


def build_index(d):
    index = dict()

    for word in d:
        letters = set(word)

        for l in letters:
            if l in index:
                index[l].add(word)
            else:
                index[l] = set()
                index[l].add(word)

    return index


def restore(text, dict):
    index = build_index(d)
    tmp = {}
    result = []

    for c in text:
        if len(tmp) == 1:
            word = tmp.pop()
            result.append(word)
            tmp = set()
        elif len(tmp) == 0:
            tmp = index[c]
        else:
            tmp = tmp & index[c]

    return " ".join(result)


if __name__ == "__main__":
    text = "ehlololwrd"
    d = {"world", "hello", "apple", "pear"}
    print restore(text=text, dict=d)
