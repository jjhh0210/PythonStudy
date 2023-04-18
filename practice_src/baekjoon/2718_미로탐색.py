from collections import deque
n,m = map(int,input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
dis = [ [0]*m for _ in range(n)]
dq = deque()
#bfs로 풀기
# 초기화
dq.append((0,0))
dis[0][0] = 1
while dq:
    now = dq.popleft()
    if now == (n-1,m-1):
        break
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0<=nx <n and 0<=ny<m and miro[nx][ny]==1:
            miro[nx][ny]=0
            dis[nx][ny] = dis[now[0]][now[1]]+1
            dq.append((nx,ny))
print(dis[n-1][m-1])
# for a in dis:
#     for x in a:
#         print(x,end=" ")
#     print()