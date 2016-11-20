"""
Given a stack, sort it values using an additional stack only.
Operations like push, pop, peel and is_empty permitted.
"""


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]

        return None

    def is_empty(self):
        return len(self.stack) == 0


def sort(arr):
    stack1 = Stack()
    stack2 = Stack()

    for x in arr:
        stack1.push(x)

    while not stack1.is_empty():
        while stack2.is_empty() or stack1.peek() >= stack2.peek():
            stack2.push(stack1.pop())

            if stack1.is_empty():
                return stack2.stack

        # If stack is already sorted
        if stack1.is_empty():
            while stack2.is_empty():
                stack1.push(stack2.pop())

            return stack1.stack

        tmp = stack1.pop()

        while not stack2.is_empty() and stack2.peek() >= tmp:
            stack1.push(stack2.pop())

        stack1.push(tmp)

        while not stack2.is_empty():
            stack1.push(stack2.pop())


if __name__ == "__main__":
    arr = [4, 3, 1, 2, 5]
    print(sort(arr))
