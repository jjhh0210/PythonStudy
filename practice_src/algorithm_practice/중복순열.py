N,M = map(int, input().split())
p = [0]*M
cnt = 0
def dfs(L):
    global cnt,p
    if L == M:
        print(*p)   # " ".join(list(map(str,p)))
        cnt+=1
        return
    for i in range(1,N+1):
        p[L] = i
        dfs(L+1)
dfs(0)
print(cnt)
