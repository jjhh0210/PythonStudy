mapp = [list(map(int, input().split())) for _ in range(10)]
ans = -1

# print(mapp[9].index(2)) # 시작할 지점 찾기(원소가 2인 곳의 위치)
start = mapp[9].index(2)

def DFS(x,y):
    if x == 0:
        print(y)
    else:
        # dx,dy 지정해서 for문 돌지 않는 이유 : 한번 길 정하면 백트래킹 필요 없기 때문!!
        if 0<=y-1 and mapp[x][y-1] == 1:    # 왼쪽으로 갈 수 있는경우
            mapp[x][y-1] = 0
            DFS(x,y-1)
        elif y+1<10 and mapp[x][y+1] == 1:  # 오른쪽으로 갈 수 있는 경우
            mapp[x][y+1] = 0
            DFS(x,y+1)
        else:
            mapp[x-1][y] = 0    # 양쪽 안되면 위로 이동
            DFS(x-1,y)

DFS(9,start)





