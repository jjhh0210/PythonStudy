import copy
import sys
from collections import deque


def compare_group(g1,g1_std,g1_cnt_normal_block, g2,g2_std,g2_cnt_normal_block):
    g1_score = (len(g1), g1_cnt_normal_block, g1_std[0], g1_std[1])
    g2_score = (len(g2), g2_cnt_normal_block, g2_std[0], g2_std[1])

    return (g1,g1_std,g1_cnt_normal_block) if g1_score > g2_score else (g2,g2_std,g2_cnt_normal_block)

def bfs(x,y,color,visited):
    global n,m
    dx = (-1, 0, 1, 0)
    dy = (0, 1, -1, 0)

    q = deque([(x,y)])
    group = deque([(x,y)])
    rainbow_visited = [[False] * n for _ in range(n)]   # 무지개 블록 전용 방문 배열

    while q:
        cx,cy = q.popleft()
        for d in range(4):
            nx, ny = cx+dx[d], cy+dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == color or board[nx][ny] == 0:
                    if board[nx][ny] > 0 and not visited[nx][ny]:  # 일반 블록 처리
                        q.append((nx, ny))
                        group.append((nx, ny))
                        visited[nx][ny] = True
                    elif board[nx][ny] == 0 and not rainbow_visited[nx][ny]:  # 무지개 블록 처리
                        q.append((nx, ny))
                        group.append((nx, ny))
                        rainbow_visited[nx][ny] = True

    return group

def is_normal_block(x,y):
    return 1<=board[x][y]<=m

def find_max_group():
    global n,m

    visited = [[False] * n for _ in range(n)]
    max_group,max_std_block,max_cnt_normal_block = deque(),(0,0),0

    for i in range(n):
        for j in range(n):
            if is_normal_block(i,j) and not visited[i][j]:   # 일반 블록일 경우만 start (어차피 1개 이상의 일반블록 포함되어야 되니까)
                color = board[i][j]
                # visited[i][j] = True
                # 그룹 완성
                group = bfs(i,j,color,visited)

                print(group)

                # 길이 2이상일 경우에만 그룹 가능
                if len(group)>=2:
                    # 무지개블록 개수 - 단순 계산이니 컴프리헨션 쓰지 x
                    cnt_normal_block = sum(1 for x,y in group if is_normal_block(x,y))
                    # 기준 블록 (일반 블록 중 행 min->열 min)
                    std_block = min((x,y) for x,y in group if is_normal_block(x,y))
                    # max_group 그룹 갱신 여부 확인
                    max_group,max_std_block,max_cnt_normal_block =compare_group(max_group,max_std_block,max_cnt_normal_block,group, std_block, cnt_normal_block)


    return max_group

def remove_blocks(group):
    for x, y in group:
        board[x][y] = -2 # 제거 됨(빈칸)
    return len(group)*len(group)


def gravity():
    # 열을 왼-> 오 순으로 진행하며 , 행을 아래에서 위로 훑어나감
    # 핵심 : 검은블록을 만날 때 까지 블록을 drop, 만나면 검블 위로 drop
    for j in range(n):
        # 현재 블록이 떨어져야 할 위치(행)
        drop_idx = n-1   # 맨 밑 n-1 부터 시작
        for i in range(n-1,-1,-1):
            # 검은 블록(-1)이 아니고, 빈칸(-2)이 아니고(>0), drop_idx보다 위에 있는 블록이면 drop
            if board[i][j]>0 and i>drop_idx:
                board[drop_idx][j] = board[i][j] #drop
                board[i][j] = -2    # 빈칸으로 대체
                drop_idx-=1
            # 검은 블록 만나면 drop_idx 변경 (검은블록 바로 위)
            elif board[i][j] ==-1:
                drop_idx = i-1

#반시계 90회전
def rotate():
    # 반시계 90회전

    # global n
    # new_board = copy.deepcopy(board)
    # for i in range(n):
    #     for j in range(n):
    #         new_board[n-1-j][i] = board[i][j]

    global board    # 배열에 아예 새로운 값 할당시에는 무조건 global board해주자!
    board = list(map(list,zip(*board)))[::-1]


#### main ####

sys.stdin = open("input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 0 # 점수

    # 오토 플레이
    while True:
        # 처음으로 일반블록이나 무지개블록인 것 찾기

        # 1. max 블록 그룹 찾기 (없으면 오토 플레이 중지)
        max_group = find_max_group()
        if not max_group:
            break

        # 2. 블록 그룹 제거 및 점수 산출
        ans+= remove_blocks(max_group)

        # 3. 중력 작용
        gravity()
        
        # 4. 반시계 회전
        rotate()

        # 5. 중력 작용
        gravity()

print(ans)


