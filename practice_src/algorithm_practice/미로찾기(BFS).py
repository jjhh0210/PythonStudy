from collections import deque
board = [list(map(int, input().split())) for _ in range(7)]

# ch = [[0]*7 for _ in range(7)]  # check는 필요없는게, board에다가 그냥 지나온자리(못가는곳) 1로체크하면 됨
dis = [[0]*7 for _ in range(7)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
dq = deque()

#루트 초기화
dq.append((0,0))
board[0][0] = 1

while dq :
    now = dq.popleft()
    for i in range(4):
        x = now[0]+dx[i]
        y = now[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and board[x][y] == 0:
            board[x][y] = 1
            dis[x][y] = dis[now[0]][now[1]]+1
            dq.append((x,y))
if dis[6][6] ==0:
    print(-1)
else:
    print(dis[6][6])


