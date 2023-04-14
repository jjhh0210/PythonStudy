import numpy as np
n = int(input())
mapp= [list(map(int, input().split())) for _ in range(n)]

ch = [[0]*n for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 출발, 목적 지점 구하기 - 2차원 배열의 최대, 최소 구하기!!!
minn = float("inf")
maxx = float("-inf")
min_pos = (0,0)
max_pos = (0,0)
for i in range(n):
    for j in range(n):
        if minn > mapp[i][j]:
            minn = mapp[i][j]
            min_pos = (i,j)
        if maxx < mapp[i][j]:
            maxx = mapp[i][j]
            max_pos = (i,j)

cnt=0
def dfs(x,y,prev_dir):
    global cnt
    if (x,y) == max_pos:
        cnt+=1
    else:
        for i in range(4):
            if prev_dir!=-1 and i == (prev_dir +2)%4:
                continue
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0 and mapp[nx][ny] > mapp[x][y] :
                ch[nx][ny]=1
                dfs(nx,ny,i)
                ch[nx][ny]=0

ch[min_pos[0]][min_pos[1]]=1  #출발지점 일단 체크
print(min_pos, max_pos)
dfs(min_pos[0],min_pos[1],-1)
print(cnt)






