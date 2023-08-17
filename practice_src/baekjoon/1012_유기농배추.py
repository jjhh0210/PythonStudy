import sys
sys.setrecursionlimit(10000)   #설정안하면 런타임오류

def dfs(m,n,x,y):
    global dx,dy

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and farm[nx][ny]==1:
            farm[nx][ny]=0
            dfs(m,n,nx,ny)

if __name__ == '__main__':
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    t = int(sys.stdin.readline())
    for _ in range(t):
        m, n, k = map(int, sys.stdin.readline().split())
        farm = [[0] * m for _ in range(n)]
        cnt = 0

        for _ in range(k):
            col,row = map(int, sys.stdin.readline().split())  #입력조건 주의 ->배열에서는 좌표 X = 열, Y = 행이다!!
            farm[row][col] = 1
        for i in range(n):
            for j in range(m):
                if farm[i][j] == 1:
                    farm[i][j] = 0  #방문된 시작 좌표는 0으로 바꾸어 놓는다.
                    cnt+=1
                    dfs(m,n, i, j)
        print(cnt)
