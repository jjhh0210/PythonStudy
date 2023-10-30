'''

2. 단순 구현 : 로봇의 2차원배열 탐색, S =유지, R = 오른쪽90회전 , L = 왼쪽90회전, OOB면 180회전
    - 더이상 방문 불가시 (루프 or 전체 다 방문) 방문한 갯수 return

'''
# setdefault : key값이 있으면 key 반환, 없으면 2번째 인자 생성

arr = ["LSSS","RSSS","SSSS","SSSS"]
N = len(arr)

dx = [1,0,-1,0] #아래, 왼, 위, 오
dy = [0,-1,0,1]

dir = 0 # 다음으로 이동할 방향, 아래로 초기화
visited = {}
x,y = 0,0   # 현재 위치
while True:
    print(visited)
    # 탈출 조건1 : 모든 그리드 탐색한 경우
    if len(visited) == N*N:
        ans = len(visited)
        break
    # 다음 방향 설정
    if arr[x][y] == "R":  # 시계
        ndir = (dir + 1) % 4
    elif arr[x][y] == "L":  # 반시계
        ndir = (dir - 1) % 4
    else:  # S일땐 그대로
        ndir = dir

    # 다음 위치 (OOB인 경우 처리)
    nx,ny = x+dx[ndir], y+dy[ndir]
    if nx<0 or ny<0 or nx>=N or ny>=N:
        ndir = (ndir+2)%4
        nx, ny = x + dx[ndir], y + dy[ndir]  # 회전 후 새로운 위치 계산


    if (x,y) in visited: # key값이 있음
        # 탈출조건1 : 해당 방향으로 이미 탐색한 경우
        if ndir in visited[(x,y)]:
            break
        else:
            visited[(x,y)].append(ndir)
    else:   # key값 없음
        visited[(x,y)] = [ndir]
    x, y, dir = nx,ny,ndir

print(len(visited))
