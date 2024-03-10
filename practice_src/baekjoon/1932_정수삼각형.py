import sys
input = sys.stdin.readline
n = int(input())    #삼각형 크기
tri = [list(map(int, input().split())) for _ in range(n)]

d = [[0]*i for i in range(1,n+1)]

d[0][0] = tri[0][0]

if n>1:
    for L in range(1,n):    # L: 0~n-1
        d[L][0] = d[L-1][0] + tri[L][0] # 첫번째 원소
        d[L][L] = d[L-1][-1] + tri[L][-1]    # 마지막 원소(L)
        for i in range(1,L):    # 2~ 마지막이전 원소까지 (1~L-1)
            # 이전 깊이의 i-1(왼), i(오) 원소 비교
            d[L][i] = max(d[L-1][i-1],d[L-1][i]) + tri[L][i]

print(max(d[n-1]))   # 인덱스가 0부터 이므로 마지막은 n-1

# for a in d:
#     print(a)

