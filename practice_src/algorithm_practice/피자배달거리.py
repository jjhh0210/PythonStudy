N,M = map(int, input().split())
mapp = [ list(map(int, input().split())) for _ in range(N)]
#1. 전체 피자집, 집 리스트 추출
ans = float("inf") #전체 피자집 조합 중 가장 최소 배달거리
stores = []
houses = []
comb = [(0,0)]*M    # 선택 된 피자집 조합 (초기화 필수)
for i in range(N):
    for j in range(N):
        if mapp[i][j] == 1:
            houses.append((i,j))

        if mapp[i][j]==2:
            stores.append((i,j))
print(*stores)
print(*houses)
#2. dfs 로 조합 탐색
def dfs(L,S):
    global ans
    if L == M:
        # 모든 집들에 대해 배달 최소 거리 구하기
        dis_summ = 0    # M개의 피자집 조합 별 총 최소 배달 거리
        for house in houses:
            dis_min = float("inf")  #각 집 마다 선택 된 피자집과의 최소 거리(따라서 집 시작할 때마다 0으로 초기화 해줘야)
            for store in comb:
                dis_min = min(dis_min, abs(house[0] - store[0]) + abs(house[1] - store[1]))
            dis_summ += dis_min
        ans = min(ans, dis_summ)    # 모든 피자집 조합에서의 최소 배달 거리
        print(*comb, dis_summ)
    else:
        for i in range(S,len(stores)):
            comb[L] = stores[i]
            dfs(L+1,i+1)

dfs(0,0)
print(ans)


        


