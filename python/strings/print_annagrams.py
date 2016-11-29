"""
Given a set of strings, print all anagrams together
"""


def collect_anagrams(words):
    d = {}

    for w in words:
        index = ''.join(sorted(w))

        if index in d:
            d[index].append(w)
        else:
            d[index] = [w]

    return d


if __name__ == "__main__":
    words = {"cat", "dog", "tac", "pot", "top", "god"}
    print(collect_anagrams(words))
