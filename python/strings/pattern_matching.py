"""
Implement regular expression matching with support for '.' and '*'.
"""


def match(text, pattern):
    if not text and not pattern:
        return True

    if not text or not pattern:
        return False

    if text[0] == pattern[0] or pattern[0] == '.':
        return match(text[1:], pattern[1:])
    elif pattern[0] == "*":
        for i in range(len(text) + 1):
            if match(text[i:], pattern[1:]):
                return True

    return False

if __name__ == "__main__":
    text = "aab"
    pattern = ".*"
    print(match(text, pattern))
    print(match("aaa", "aa"))
    print(match("abba", "a.b*"))
    print(match("aab", "c*a*b"))
