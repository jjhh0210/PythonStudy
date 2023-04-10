n,m = map(int, input().split())
comb=[0]*m
cnt=0
def dfs(L,S):
    global cnt
    if L==m:
        cnt+=1
        print(*comb)
    else:
        for i in range(S,n+1):
            comb[L] = i
            dfs(L+1,i+1)

dfs(0,1)
print(cnt)