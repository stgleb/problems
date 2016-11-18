"""
Implement stack with push, pop and min functions
working in O(1)
"""


class Stack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)

        if len(self.min_stack) == 0 or self.min_stack[-1] > value:
            self.min_stack.append(value)

    def pop(self):
        value = self.stack.pop()

        if len(self.min_stack) > 0 and value == self.min_stack[-1]:
            self.min_stack.pop()

        return value

    def get_min(self):
        if len(self.min_stack) > 0:
            return self.min_stack[-1]

        return None

if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    stack.push(4)
    print(stack.get_min())
    stack.push(1)
    print(stack.get_min())
    stack.push(5)
    stack.push(0)
    print(stack.get_min())
    stack.pop()
    print(stack.get_min())
