board= [list(map(int, input().split())) for _ in range(7)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0

board[0][0] = 1
def dfs(x,y,prev_dir):
    global cnt
    if x==6 and y==6:
        cnt+=1
    else:
        for i in range(4):
            if prev_dir!=-1 and i == (prev_dir + 2) % 4:    # 미로탐색같은 특정 문제에서 출발지점으로 돌아갈 것 (이전에 탐색한 방향과 반대로 들어갈 것 방지)
                continue
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
                board[xx][yy]=1
                dfs(xx,yy,i)
                board[xx][yy]=0
dfs(0,0,-1)
print(cnt)