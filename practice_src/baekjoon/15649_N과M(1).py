import sys
input=sys.stdin.readline
n,m = map(int, input().split())

def dfs(depth):
    global n,m
    if depth == m:
        print(*comb)
    else:
        for i in range(1,n+1):
            if not ch[i]:   # 방문 안했으면
                comb[depth] = i
                ch[i]=True
                dfs(depth+1)
                ch[i] = False

ch = [False]*(n+1)
ans = []
comb = [0]*m
# dfs(0)

#### permutations사용
from itertools import permutations
pers = permutations([i for i in range(1,n+1)],m)
for p in pers:
    print(*p)
