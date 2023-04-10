n = int(input())
p = list(map(int,input().split()))
m = int(input())
res = float("inf") # 동전 개수 최소값
p.sort(reverse=True)

def dfs(L,summ):
    global res, p
    if summ > m or L>=res:  # 이미 찾아놓은 최소 동전 수보다 더 많은 개수를 탐색할 필요 없음
        return
    if summ == m:
        res = L       # if L < res : res = L 더 적은 수의 동전 찾으면 갱신
    else:
        for i in range(n):
            dfs(L+1, summ+p[i])

dfs(0,0)
print(res)