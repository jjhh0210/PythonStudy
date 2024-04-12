'''

<조건>
- 1루돌프 : 1~p번 산타들
- 루돌프 -> 산타 박치기 해서 산타 선물 배달 방해 / 산타 -> 루돌프 잡아야
- nxn크기 격자, (1,1)⭐️부터 시작!!
- 두 칸 사이 거리 : 행차이제곱 + 열차이제곱

<input>
5 7 4 2 2   #n게임판크기 m게임턴 p산타수 c루돌프힘 d산타힘

3 2         # 루돌프 초기 위치 (i,j)

1 1 3       # p만큼 : 산타 번호, 산타초기위치 i, j
2 3 5
3 5 1
4 4 4
'''


import sys
input = sys.stdin.readline

N,M,P,C,D = map(int, input().split())
maps = [ [0]*(N+1) for _ in range(N+1)] # 1,1부터라서
dolf_r, dolf_c = map(int, input().split())  # [ r, c ]

santas = { 'pos':[(0,0)]*(P+1),
           'stop': [0]*(P+1),
           'score': [0]*(P+1)}

# 위부터 시계방향
# 상하좌우 : 0,2,4,6
# 대각선: 1,3,5,7
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

def cal_dist(r,c,r2,c2):
    return (r-r2)*(r-r2) + (c-c2)*(c-c2)

def crash_santa(st, d, z):# 산타번호, 이동할방향, 몇칸이동할건지(+점수)
    sr,sc = santas['pos'][st]
    maps[sr][sc] = 0
    # 점수 부여
    santas['score'][st] += z
    # 기절 처리
    santas['stop'][st] = 2
    # 이동
    # OOR : 탈락 / 산타 있음: 이동, 상호작용 / 빈칸: 이동
    nsr, nsc = sr+dr[d]*z, sc+dc[d]*z
    while True:
        # OOR: 탈락!! maps에서 산타 없애기
        if not (1<=nsr<=N and 1<=nsc<=N):
            santas['pos'][st] = (0,0)
            return
        # 빈칸: 이동 후 break (위치,maps 업데이트)
        if maps[nsr][nsc] == 0:
            maps[nsr][nsc] = st
            santas['pos'][st] = (nsr,nsc)
            return
        else:
            santas['pos'][st] = (nsr,nsc)
            # 옮길 산타 번호(st) 업데이트
            temp = maps[nsr][nsc]   # 원래 있던 산타 빼고
            maps[nsr][nsc] = st     # 옮길 산타 안착
            st = temp               # 원래 있던 산타를 옮길 산타로 업데이트!!
            sr, sc = santas['pos'][st]
            nsr,nsc = sr+dr[d], sc+dc[d]

for _ in range(P):
    num, r, c = map(int, input().split())
    maps[r][c] = num
    santas['pos'][num] = (r,c)

for _ in range(M):
    ### 1. 루돌프 이동
    # 1) 돌진할 산타 선정
    real_st = None      # 돌진할 산타 (최소 거리)
    min_dist = None     # 해당 산타와의 현재 거리
    for st in range(1,P+1):
        sr, sc = santas['pos'][st]
        dist = cal_dist(sr, sc, dolf_r, dolf_c)
        if (sr,sc)!= (0,0):    #탈락안한 산타라면!!
            if real_st is None or (min_dist,sr,sc) > (dist,santas['pos'][real_st][0], santas['pos'][real_st][1]):
                real_st = st
                min_dist = dist
    # 2) 해당 산타와 가장 가까워지는 방향 정하기
    sr,sc = santas['pos'][real_st]
    min_d = 0
    for d in range(8):
        dolf_nr, dolf_nc = dolf_r+dr[d], dolf_c+dc[d]
        if 1<=dolf_nr<=N and 1<=dolf_nc<=N:
            dist = cal_dist(dolf_nr,dolf_nc,sr,sc)
            if dist < min_dist:
                min_dist = dist
                min_d = d
    # 루돌프 한칸 이동
    dolf_r, dolf_c = dolf_r + dr[min_d], dolf_c + dc[min_d]
    # 충돌 발생시, 산타 이동시키기
    if (dolf_r, dolf_c) == (sr, sc) :
        crash_santa(real_st,min_d,C)

    ### 2. 산타 이동
    for st in range(1,P+1):
        # 기절 햇거나 탈랙했으면 이동X
        sr,sc = santas['pos'][st]
        if santas['stop'][st]>0 or (sr,sc)==(0,0) :
            continue
        # 루돌프와 가장 가까워지는 이동 방향 구하기
        min_dist = cal_dist(sr,sc,dolf_r,dolf_c)
        min_d = 0
        for d in [0,2,4,6]: # 상 우 하 좌
            nsr, nsc = sr+dr[d], sc+dc[d]
            if 1 <= nsr <= N and 1 <= nsc <= N and maps[nsr][nsc]<=0:    # OOR 아니고, 다른 산타 있지 않고
                dist = cal_dist(dolf_r, dolf_c, nsr, nsc)
                if dist < min_dist:
                    min_dist = dist
                    min_d = d
        # min_dist가 갱신이 됐을 경우에만 이동 (더 가까워졌을 경우에만!)
        if min_dist < cal_dist(sr,sc,dolf_r,dolf_c):
            maps[sr][sc] = 0
            sr,sc = sr + dr[min_d], sc + dc[min_d]
            maps[sr][sc] = st
            santas['pos'][st] = (sr,sc)
            # 충돌 발생시, 산타 이동시키기
            if (dolf_r, dolf_c) == (sr, sc):
                crash_santa(st, (min_d+4)%8, D)

    # 3. 턴 종료) 탈락 안한 산타 점수 부여, 기절 한 산타 기절 풀기
    tal_cnt = 0
    for st in range(1,P+1):
        r,c = santas['pos'][st]
        if (r,c) == (0,0):
            tal_cnt+=1
        else:
            santas['score'][st] +=1
            if santas['stop'][st]>0:
                santas['stop'][st]-=1
    # 만약 모두 탈락했다면 게임 종료
    if tal_cnt == P:
        break

print(*santas['score'][1:])





'''
# 위부터 시계방향
# 상하좌우 : 0,2,4,6
# 대각선: 1,3,5,7
dr = [-1,-1,0,1,1,1,0,-1] 
dc = [0,1,1,1,0,-1,-1,-1]

루돌프랑 거리 계산: cal_dist()

- for _ in range(m):
    
    1. 루돌프 1칸 돌진 (8방)
    
        a. 루돌프는 탈락안한⭐ 산타 중 가장 가까운 산타 1개 선정
           산타 여러개면 선정 기준 : 루돌프 산타와의 거리 짧 -> r 좌표 큼 -> c 좌표 큼⭐
            st_num= max(range(len(santas)), key=lambda x: (santas[x][0][1], santas[x][0][0], santas[x][1])) 
            근데 조건 있으니까 그냥 for...       
        b. 그 산타한테 8방향 중 가장 가까워지는 방향으로 한칸 돌진
            for문으로 구현
        c. if (루 == 산 같은칸 됨) : 충돌
    2. for 1번~p번 산타 순서대로 한 번씩 움직임 (상하좌우 4방)
        a. 이동 산타 조건: if 기절 안함, 게임에서 탈락 안함⭐
        b. 루돌프에게 가장 가까워지는 방향으로(상하좌우)!! 가능하면 1칸 이동(멀어지는 방향은x)
            - 가장 가까울 수 있는 방향 조건: 딴 산타있는 곳 아님 and OOR가 아님 and 산-루 거리 제일 줄어듦
            - 가장 가까워질 수 있는 방향 여러개시 우선순위: 상> 우> 하> 좌⭐
        if 기절 안함, 게임에서 탈락 안함:
            for  d in [0,2,4,6]:
                가장 가까워질 수 있는 방향 찾기
            글로 이동
        
        c. if (루 == 산 같은칸 됨) : 충돌

    3. if 산타 모두 탈락? 게임종료 break

    4. 아직 탈락하지 않은 산타들에게는 1점씩을 추가로 부여
- 게임이 끝났을 때 각 산타가 얻은 최종 점수를 1~P 순서대로 공백두고 출력
  
- 충돌
루돌프가 움직여서 충돌이 일어난 경우, 해당 산타는 C만큼의 점수를 얻게 됩니다. 이와 동시에 산타는 루돌프가 이동해온 방향으로 C 칸 만큼 밀려나게 됩니다.
산타가 움직여서 충돌이 일어난 경우, 해당 산타는 D만큼의 점수를 얻게 됩니다. 이와 동시에 산타는 자신이 이동해온 반대 방향으로 D 칸 만큼 밀려나게 됩니다.
    해당 산타 점수 부여 (루돌프 돌진 or 산타 돌진 다름)
    a. 해당 산타 위치 이동 (루돌프 돌진 경우 or 산타 이동 경우 다름!)
    b. 해당 산타 기절 처리
        - k번째 턴? k+1번째 턴까지 기절, k+2부터 정상 (움직일 수만 없지, 충돌이나 상호작용으로 밀려남 ㄱㄴ)

- 상호작용
     산타는 충돌 후 착지하게 되는 칸에 다른 산타가 있다면
     그 산타는 1칸 해당 방향으로 밀려나게 됩니다.
     그 옆에 산타가 있다면 연쇄적으로 1칸씩 밀려나는 것을 반복하게 됩니다.
     게임판 밖으로 밀려나오게 된 산타의 경우 게임에서 탈락됩니다.
'''