'''
<조건>
- n가지 종류의 동전이 있다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다.
- 가능한 경우의 수 (동전 조합) 구하기
- 동전 중복 사용 가능

<input>
3 10    #n 동전 종류, k원 만들기
1       # 동전들
2
5

<output>
10
--------------
   0 1 2 3 4 5 6 7 8 9 10
0  1 0 0 0 0 0 0 0 0 0 0
1  1 1 1 1 1 1 1 1 1 1 1
2  1 1 2 2 3 3 4 4 5 5 6
5  1 1 2 2 3 4 5 6 7 8 10(6+4)
d[i][j] = 동전 i 에 대해 j 원 만들 때 가능한 경우의 수
-> 0-1 냅색문제 : 12865 평범한 배낭 문제랑 같이 보기
'''
import sys
input = sys.stdin.readline

n,k = map(int, input().split())

## 2차원 배열 -> 메모리 초과!
# d = [[0]*(k+1) for _ in range(n+1)]
# d[0][0] = 1

# for i in range(1,n+1):
#     coin = int(input())
#     # i: 동전 번호, coin: 해당 동전의 가치(원), j: 만들 금액
#     for j in range(k+1):
#         if j < coin:
#             d[i][j] = d[i-1][j]
#         else:
#             d[i][j] = d[i-1][j] + d[i][j-coin]
#
# print(d[n][k])

## 1차원 배열로
d = [0]*(k+1)
d[0]=1
for _ in range(n):
    coin = int(input())
    for j in range(k+1):
        if j >= coin:
            d[j] = d[j] + d[j-coin]

print(d[k])
