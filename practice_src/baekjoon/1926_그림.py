'''
- 입력
세로크기n, 가로크기m
그림이차원배열

- 출력 :
그림의 개수
max 그림의 넓이

- 주의
그림이 하나도 없는 경우, 가장 넓은 그림의 넓이 = 0
'''

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())  # 세로(i), 가로(j)
arr = [list(map(int, input().split())) for _ in range(n)]    #그림
q = deque()
di = [-1,0,1,0]
dj = [0,1,0,-1]
num = 0 # 그림 개수
maxx = 0 # 그림 최대 넓이
def bfs(i,j):
    global maxx,n,m
    q.append((i,j)) #초기 방문 좌표
    arr[i][j] = 0   #방문 표시
    area = 1    # 넓이

    while(q):
        ci,cj = q.popleft() #현재 좌표
        for d in range(4):
            ni,nj = ci+di[d], cj+dj[d] #다음 좌표
            # OOB가 아니고, 방문되지 않은 좌표만 방문
            if 0<=ni<n and 0<=nj<m and arr[ni][nj]==1:
                q.append((ni,nj))
                arr[ni][nj]=0
                area+=1
    maxx = max(maxx, area)

# 도화지 전체 탐색
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            # 1이면 bfs 탐색
            num+=1
            bfs(i,j)
print(num)
print(maxx)
