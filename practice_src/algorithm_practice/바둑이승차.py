c,n = map(int, input().split())
w = []
for _ in range(n):
    w.append(int(input()))
maxx = float("-inf")
total = sum(w)

# tsum = 이때까지 거쳐온 애들의 합 (선택 했든 안했든)
# total - tsum = 선택지에 남은 애들의 합
def dfs(v,summ,tsum):
    global maxx, total
    if summ>c or total-tsum+summ < maxx:
        # 더했더니 총합이 c보다 더 커지면 탐색 x or 현재 summ에서 밑에 남은애들(total-tsum)) 다 더해도 maxx보다 작으면 탐색 x
        return
    if v == n:
        maxx = max(maxx,summ)
    else:
        dfs(v+1,summ+w[v],tsum+w[v])  # w[v] 선택
        dfs(v+1,summ,tsum+w[v])       # w[v] 선택 x
dfs(0,0,0)
print(maxx)