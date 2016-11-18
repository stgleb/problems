"""
Implement queue with two stacks
"""


class Queue(object):
    def __init__(self):
        self.first = []
        self.second = []

    def push(self, value):
        self.first.append(value)

    def pop(self):
        while self.first:
            value = self.first.pop()
            self.second.append(value)

        return self.second.pop()


if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
