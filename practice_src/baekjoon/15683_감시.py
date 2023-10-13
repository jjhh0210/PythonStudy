import sys
import copy

def watch(temp, dirs, x, y, cnt):
    global n, m
    for dir in dirs:
        nx,ny = x,y
        # 해당 방향으로 영역 fill
        while True:
            nx = nx + dx[dir]
            ny = ny + dy[dir]
            if nx<0 or nx>=n or ny<0 or ny>=m or temp[nx][ny] ==6:    # OOB, 벽만남 -> fill stop
                break
            if temp[nx][ny]==0:
                cnt-=1
                temp[nx][ny] = 7
    return cnt

def dfs(board, depth, cnt):  #depth = 현재 몇번째 cctv인지!!
    global ans
    # 종료 조건 :  모든 cctv 방향 설정 완료.(한개의 조합 완성)
    if depth == len(cctv_list):
        # 사각지대 cnt, 최소 사각 지대 ans랑 비교
        ans = min(ans, cnt)
        return
    #  종료 조건이 아니면
    temp = copy.deepcopy(board) #보드 복제
    now_cctv_mode,x,y = cctv_list[depth]    # 현재 cctv
    
    # 현재 cctv 감시 방향 모두 탐색하면서
    for dir in mode[now_cctv_mode]:
        # 해당 방향으로 영역에 모두 fill
        next_cnt = watch(temp,dir,x,y, cnt)
        # 이 상태로 다음 cctv의 dfs 호출
        dfs(temp, depth+1,next_cnt)
        # 다른 dir 적용하기 전에 보드 영역 watch 이전 으로 초기화
        temp = copy.deepcopy(board)

#### main ####

sys.stdin = open("input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int, input().split())     #세로(행수), 가로(열수)
    ans = n*m       #사각지대 영역 최소값 초기화
    cctv_list = []  #[번호, i, j]
    board = [[0]*m for _ in range(n)] # 배열 초기화

    # board 배열 입력 받고 cctv_list 만들기
    for i in range(n):
        row = list(map(int,input().split()))
        for j in range(m):
            board[i][j] = row[j]
            if 1<=row[j]<=5:    #cctv인 경우 list에 적립
                cctv_list.append([row[j],i,j])
                ans-=1
            elif row[j] == 6:
                ans-=1

    # 0:서 1:북 2:동 3:남(<-부터 시계 방향)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    # cctv번호 별 방향 조합 설정
    mode = {
        1:[[0],[1],[2],[3]],
        2: [[0,2],[1,3]],
        3: [[0,1],[1,2],[2,3],[3,0]],
        4: [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
        5: [[0,1,2,3]],
    }
    # dfs로 각 cctv 방향 조합 탐색
    dfs(board,0, ans)
    print(ans)
