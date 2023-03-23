from collections import deque

n = int(input())


def checkVPS(s):
    d = deque() #매번 스택이 초기화 되어야 하니까
    for p in s:
        if p == '(':
            d.append('(')
        else:
            if len(d)==0:
                return "NO"
            d.pop()
    if d: #empty -> False, not empty -> True
        return "NO"
    else:
        return "YES"


for _ in range(n):
    ps = input()
    print(checkVPS(ps))
