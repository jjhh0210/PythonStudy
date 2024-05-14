'''
<조건>
- N개의 물건 (W,V)
- 최대 K 무게 가능한 배낭
- 물건 가치 합의 최댓값을 출력

<input>
4 7     # 물품 수 N, 최대 무게 K
6 13    #  각 물건의 W, V
4 8
3 6
5 12

<output>
14

'''
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
d = [[0]*(k+1) for _ in range(n+1)]    # 물건 0: 아무것도 안넣음 의미. 따라서 물건은 1~n까지!

# 첫번째 물건부터 마지막 물건까지 따져보며 최종 최대 가치 산출
for i in range(1, n+1):
    w,v = map(int, input().split())

    # i 물건에 대해 배낭 max 무게별(j) 최대 가치 설정
    for j in range(1,k+1):
        if j < w:       # 배낭 max무게 < 물건 무게 : 해당 물건 못넣음
            d[i][j] = d[i-1][j]
        else:           # 배낭 max무게 <= 물건 무게 : 해당 물건을 넣을 수 있음
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)     # max( 해당 물건 안 넣었을때 가치, 해당 물건 넣었을 때 가치)

print(d[n][k])
