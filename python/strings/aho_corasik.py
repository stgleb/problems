"""
Implement Aho-Corasik algorithm
"""


class Node(object):
    def __init__(self, char, is_root=False):
        self.char = char
        self.suffix_link = None
        self.children = {}
        self.is_root = is_root


def build_trie(text):
    root = Node(char='', is_root=True)
    parent = root

    for c in text:
        if c not in parent.children:
            node = Node(char=c)
            parent.children[c] = node

        if parent.is_root:
            node.suffix_link = parent

        p = parent
        cur = node

        while not p.is_root:
            if c not in p.suffix_link.children:
                new_node = Node(c)
                p.suffix_link.children[c] = new_node

            cur.suffix_link = p.suffix_link.children[c]
            cur = cur.suffix_link
            p = p.suffix_link

        cur.suffix_link = root
        parent = node

    return root


def find_word(word, trie):
    cur_node = trie

    for c in word:
        if c not in cur_node.children:
            return False

        cur_node = cur_node.children[c]

    return True


if __name__ == "__main__":
    text = "abcdedacbae"
    word1 = "dbc"
    word2 = "acb"
    word3 = "edc"
    word4 = "dacb"
    trie = build_trie(text)
    print(find_word(word1, trie))
    print(find_word(word2, trie))
    print(find_word(word3, trie))
    print(find_word(word4, trie))
