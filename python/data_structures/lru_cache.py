class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class LRUCache(object):
    def __init__(self, size):
        self.size = size
        self.d = {}
        self.l = []

    def put(self, key, value):
        if len(self.l) == self.size:
            node = self.l[0]
            self.l = self.l[1:]
            del self.d[node.key]

        node = Node(key, value)
        self.l.append(node)
        self.d[key] = node

    def get(self, key):
        if key not in self.d:
            return None

        node = self.d[key]
        # Ideally should be done on linked list
        self.l.remove(node)
        self.l.append(node)
        return node.value


if __name__ == "__main__":
    lru = LRUCache(3)
    lru.put(1, "hello")
    lru.put(2, "world")
    lru.put(3, "spam")
    print(lru.get(1))
    lru.put(4, "will delete one")
    print(lru.get(1))

