def DFS(L, sum):
    global cnt
    if sum==m:
        cnt+=1
        return
    if L==n or sum>m:
        return
    # if sum>m:
    #     return
    # if L==n:
    #     if sum==m:
    #         cnt+=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*i))

m=int(input())
n=int(input())
cv=list()
cn=list()
for i in range(n):
    a, b=map(int, input().split())
    cv.append(a)
    cn.append(b)
cnt=0
DFS(0, 0)
print(cnt)