"""
Given a stack, sort it using recursion. Use of any loop constructs like while,
for..etc is not allowed. We can only use the following ADT functions on Stack S
"""


def stack_sort(stack):
    if stack:
        tmp = stack.pop()
        stack_sort(stack)
        stack_insert(stack, tmp)


def stack_insert(stack, element):
    if not stack or element > stack[-1]:
        stack.append(element)
    else:
        tmp = stack.pop()
        stack_insert(stack, element)
        stack.append(tmp)


if __name__ == "__main__":
    stack = [30, 14, 18, -5, -3]
    stack_sort(stack)
    print(stack)
