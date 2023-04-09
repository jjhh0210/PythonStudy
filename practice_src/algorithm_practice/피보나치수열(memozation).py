n = int(input())
fibo = [0]*(n+1)
fibo[1]=1
fibo[2]=1
def dfs(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if fibo[n]>0:
        return fibo[n]
    else:
        fibo[n] = dfs(n-1) + dfs(n-2)
        return  fibo[n]
dfs(n)
print(*fibo[1:n+1])