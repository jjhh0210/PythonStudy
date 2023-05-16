n = int(input())
mapp = [list(map(int, input())) for _ in range(n)]
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def dfs(x,y):   # 호출 후 0으로 체크하고 집 셈 -> 체크하고 집세고 호출해도 됨
    global cnt  # immutable 자료형(기본 자료형)
    mapp[x][y] = 0 #mutable 자료형(참조 변수)
    cnt+=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<n and mapp[nx][ny] == 1:
            dfs(nx,ny)

ans = []
for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1:
            cnt = 0
            dfs(i,j)
            ans.append(cnt)

ans.sort()
print(len(ans))
print(*ans)

