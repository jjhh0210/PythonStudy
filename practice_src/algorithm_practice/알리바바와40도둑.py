# # bottom-up
# n=int(input())
# arr=[list(map(int, input().split())) for _ in range(n)]
# dy=[[0]*n for _ in range(n)]    # DP 배열, (0,0) ~ 현재까지 가는데 최소비용
# dy[0][0]=arr[0][0]
# for i in range(1, n):           # 갈 수 있는 방향이 왼쪽, 아래 밖에 없으므로 가장자리는 그냥 누적하여 초기화
#     dy[0][i] = dy[0][i-1] + arr[0][i]
#     dy[i][0] = dy[i-1][0] + arr[i][0]
# for i in range(1,n):
#     for j in range(1,n):
#         dy[i][j] =  min(dy[i-1][j], dy[i][j-1]) + arr[i][j]# 왼, 위 중 작은것 + 현재 비용 = 현재까지 최소비용
#
# print(dy[n-1][n-1])

# top-down

n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
dy=[[0]*n for _ in range(n)]

def DFS(x,y):
    # 종료지점 = 출발지
    if x==0 and y==0:
        return arr[0][0]

    else:
        if y==0:
            # 위로만 올라가야 함
            dy[x][y] = DFS(x-1,y)+arr[x][y]
        elif x == 0:
            # 왼족으로만 가야함
            dy[x][y] = DFS(x,y-1) +arr[x][y]
        else:
            dy[x][y] = min(DFS(x-1,y), DFS(x,y-1)) + arr[x][y]
        return dy[x][y]



print(DFS(n-1, n-1))