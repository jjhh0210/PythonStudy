import sys
n = int(sys.stdin.readline())
stack = []


def push(a):
    stack.append(a)


def pop():
    if len(stack) == 0:
        return -1
    return stack.pop()


def size():
    return len(stack)


def empty():
    if len(stack) == 0:
        return 1
    return 0


def top():
    if len(stack) == 0:
        return -1
    return stack[-1]


for _ in range(n):
    il = sys.stdin.readline().split()
    if il[0] == "push":
        push(il[1])
    elif il[0] == "pop":
        print(pop())
    elif il[0] == "size":
        print(size())
    elif il[0] == "empty":
        print(empty())
    else:
        print(top())
