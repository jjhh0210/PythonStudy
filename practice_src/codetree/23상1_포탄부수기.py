'''
NXM격자 , 격자 이어짐!!
포탑 공격력 0이하 -> 부서진 포탑. 공격x

K턴 반복 -> 부서지지 않은 포탑==1개: 즉시 중지

1. 공격자 선정 (부서진 포탑 제외!!!)
- 가장 약한 포탑 선정 -> N+M만큼 공격력 증가
    - 선정기준: 공격력 가장 낮은 -> 최근에 공격(모두시점0에공격했엇음) -> 행+열 합 큰-> 열 큰

2. 공격
0) 공격 대상 선정 : 공 높 -> 가장 오래전 공격 -> 행+열 작은 -> 열 작은
1) 레이저 공격 먼저 시도 :
- 레이저 최단경로 선정: 우/하/좌/상 우선순위로 이동, 0으로 이동 불가, 가장자리는 반대편으로 나옴
   -> 경로 없으면 포탄 공격으로 이동
- 공격 : 공격대상)공격자의 공격력 만큼 피해입음, 경로에있는 포탑)공격력//2만큼 피해


2) 공격대상까지 레이저 도달 불가(경로x)시 포탄 공격:
- 공격대상) 공격자의 공격력 만큼 피해
- 주위 8개 방향의 포탑) 공격력//2 -> 공격자 제외!!!!!

3. 포탑 부서짐 (0이하면 0됨)

4. 정비
- 공격과 무관했던 포탑(공격자/피해자 아닌 애들) 공격력+1


경로 추적!!!
visited[i][j] => 이전에 방문한 노드를 넣어놓기!!
반대편 : ci+di % N, cj+dj % M

turn[][] = 턴수
si,sj # attacker
ei,ej # target
fset = 공격자, 피해자, 추가 피해자들
'''

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]  # 공격한 턴수를 기록(최근공격 체크)

from collections import deque

# 레이저 공격
def bfs(si,sj,ei,ej):
    q = deque()
    # for 경로 추적!!!!!
    v = [[ () for _ in range(M)] for _ in range(N)] # visited 배열!!! 나로 온 이전 위치 저장

    q.append((si,sj))
    v[si][sj] = (si,sj) # 공격자는 공격자로부터 옴
    d = arr[si][sj] # 데미지
    while q:
        ci,cj = q.popleft()
        if (ci,cj) == (ei,ej):  #목적지 좌표에 도달하면 공격 후 종료
            # 타겟 포탑에 공격자의 공격력 만큼 피해주기
            arr[ei][ej] = max(0, arr[ei][ej]-d)
            # 이때까지 온 경로들에도 추가 피해 주기
            while True:
                ci, cj = v[ci][cj]  # 직전 좌표
                if (ci, cj) == (si, sj):  # 시작(공격자)까지 되집어 왔으면 종료
                    return True
                arr[ci][cj] = max(0, arr[ci][cj] - d // 2)
                fset.add((ci, cj))

        # 우선순위: 우/하/좌/상
        for di,dj in ((0, 1),(1,0),(0,-1),(-1,0)):
            ni,nj = (ci+di)%N, (cj+dj)%M
            # 미방문이자, 포탑 있으면 방문
            if  len(v[ni][nj])==0 and arr[ni][nj] >0:
                q.append((ni,nj))
                v[ni][nj] = (ci,cj) # 내가 온 곳을 방문배열에 지정


    return False    # 목적지 못찾음
# 포탄 공격
def bomb(si,sj,ei,ej):
    d = arr[si][sj]
    # 공격대상 공격
    arr[ei][ej] = max(0, arr[ei][ej]-d)
    # 목표좌표 주변 8개에 절반 피해
    for di,dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
        # 반대편 연결!!
        ni,nj = (ei+di)%N, (ej+dj)%M
        # 공격자/부서진 포탑이면 피해X
        if arr[ni][nj]>0 and (ni,nj)!=(si,sj):
            arr[ni][nj] = max(0, arr[ni][nj]-d//2)
            fset.add((ni,nj))

for T in range(1, K + 1):
    # [1] 공격자 선정: 공격력 낮은->가장 최근 공격자->행+열(큰)->열(큰)
    mn, mx_turn, si, sj = 5001, 0, -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0:    continue    # 포탑이 아니면 skip
            if (mn,turn[i][j],i+j,j ) > (arr[i][j], mx_turn,si+sj,sj):
                mn, mx_turn, si,sj = arr[i][j], turn[i][j], i,j

    # [2] 공격(공격당할 포탑선정) & 포탑부서짐
    # 2-1) 공격 당할 포탑 선정: 공격력 높은->가장 오래전 공격->행+열(작은)->열(작은)
    mx, mn_turn, ei, ej = 0, T, N, M
    for i in range(N):
        for j in range(M):
            if arr[i][j]<=0:    continue    # 포탑이 아니면 skip
            if (mx,turn[i][j],i+j,j ) < (arr[i][j], mn_turn,ei+ej,ej):
                mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j   # si,sj 공격자

    # 2-2) 레이저공격 (우하좌상 순서로 최단거리이동-BFS, %N, %M 처리 필요(양끝연결))
    arr[si][sj]+=N+M    # 공격자는 공격력 상승, 즉시 반영 시 가장 센 포탑이 될 수도 있음
    turn[si][sj] = T    # 이번턴에 공격
    fset = set()
    fset.add((si,sj))
    fset.add((ei,ej))
    if bfs(si,sj,ei,ej)==False: # 레이저 공격 실패(False반환하면)

        # 2-3) 포탄공격
        bomb(si,sj,ei,ej)

    # [3] 포탑 정비(공격안한애들 +1)
    for i in range(N):
        for j in range(M):
            if arr[i][j]>0 and (i,j) not in fset:
                arr[i][j]+=1

    cnt = N*M
    for lst in arr:
        cnt-=lst.count(0)   # 0의 개수 세기
    if cnt<=1:   # 포탑 1개 이하면 즉시 종료
        break

print(max(map(max, arr)))   # 가장 공격력 높은 포탑의 공격력 출력