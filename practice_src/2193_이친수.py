'''

10
100 101
1000 1001 1010
10000 10001 10010 10100 10101   0: 이전거 전체 개수, 1: 이전거에서 0인 개수

1) 0: 0, 1: 1 = 전체 1
2) 0: 1, 1: 0 = 전체 1
3) 0: 1, 1: 1 = 전체 2
4) 0: 2, 1: 1 = 전체 3
5) 0: 3, 1: 2 = 전체 5
6) 0: 5, 1: 3  = 전체 8
7) 0: 8, 1: 5 = 전체 13
8) 0: 13, 1: 8 = 전체 21

<n자리에서의 이친수>
마지막이 0인 개수: 이전거 전체 개수
마지막이 1인 개수: 이전거에서 마지막이 0인 개수

전체 개수 = 마지막이 0인것 + 마지막이 1인것
'''


import sys
input = sys.stdin.readline

n = int(input())
d = [(0,0)]*91  # n= 1~90, d = (마지막이0인 개수, 마지막이 1인 개수)

d[1] = 0,1  # 한자리 수 이친수는 1 -> 전체 1개, 마지막0인거 0개
for i in range(2,n+1):
    d[i] = d[i-1][0] + d[i-1][1], d[i-1][0] # 0: 이전거 전체 개수, 1: 이전거 0 개수
print(d[n][0]+d[n][1])  #전체 = 0인거+1인거

