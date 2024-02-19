import sys
input = sys.stdin.readline

n = int(input())
costs = [ list(map(int, input().split())) for _ in range(n)]
'''
1. 테이블 정의
d[i][0] = i번째 집까지 R로 칠했을 때 비용의 최솟값
d[i][1] = i번째 집까지 G로 칠했을 때 비용의 최솟값
d[i][2] = i번째 집까지 B로 칠했을 때 비용의 최솟값

2. 점화식 (이전 집 - 현재와 다른 색깔 비용 중 최소값 + 현재 비용) 
d[i][0] = min( d[i-1][1], d[i-1][2] ) + costs[i][0]
이하 동일

3. 초기값
d[0] = costs[0]
'''
d = [[0]*3 for _ in range(n)]
d[0][:] = costs[0]  # d[0]의 원소들을 costs[0]의 원소값으로 초기화

for i in range(1,n):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + costs[i][0]   #R
    d[i][1] = min(d[i-1][0], d[i-1][2]) + costs[i][1]   #G
    d[i][2] = min(d[i-1][1], d[i-1][0]) + costs[i][2]   #B

print(min(d[-1]))
