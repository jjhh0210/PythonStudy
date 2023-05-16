from collections import deque
n = int(input())
mapp = [list(map(int, input())) for _ in range(n)]
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def bfs(x,y):
    dq = deque()
    #1. 초기화
    mapp[x][y]=0
    dq.append((x,y))
    cnt = 1
    while dq:
        now = dq.popleft()
        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n and mapp[nx][ny] == 1:
                dq.append((nx,ny))
                mapp[nx][ny]=0
                cnt+=1
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if mapp[i][j] ==1:
            cnt = bfs(i,j)
            ans.append(cnt)

ans.sort()
print(len(ans))
print(*ans)
