n,k = map(int,input().split())
nums = list(map(int,input().split()))
m = int(input())
cnt=0
def dfs(L,s, summ):
    global cnt
    if L == k:
        if summ%m == 0:
            cnt+=1
    else:
        for i in range(s,n):
            dfs(L+1,i+1,summ+nums[i])   #주의) L에서 i번째 -> L+1에선 i+1번째부터 뽑음(s = i+1)
dfs(0,0,0)
print(cnt)