"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to
endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5
"""


alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]


def get_adjacent(word):
    for i in range(len(word)):
        for c in alphabet:
            yield word[:i] + c + word[i + 1:]


def build_graph(word_list):
    """
    Build graph of transitions between word
    :param word_list:
    :return: dict
    """
    graph = {}
    word_set = set(word_list)

    for w in word_list:
        graph[w] = set()

        for adj_word in get_adjacent(w):
            if adj_word in word_set and adj_word != w:
                graph[w].add(adj_word)

    return graph


def word_ladder(begin, end, word_list):
    """
    Returns None if conversion is not possible or list of words - path
    """
    graph = build_graph(word_list)
    q = [[begin]]

    while q:
        tmp = []
        path = q[0]
        begin = path[-1]

        if begin == end:
            return path

        for word in graph[begin]:
            if word not in path:
                tmp.append(path + [word])

        q += tmp
        q = q[1:]


if __name__ == "__main__":
    begin = "hot"
    end = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(word_ladder(begin, end, word_list))
