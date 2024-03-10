from collections import deque

def solution(worldmap):
    answer = 0

    di = [0,1,1,1,0,-1,-1,-1]
    dj = [1,1,0,-1,-1,-1,0,1]

    rows = len(worldmap)
    cols = len(worldmap[0])

    dist = [[0]*cols for _ in range(rows)]
    q = deque()
    q.append((0,0))

    while q:
        ci,cj = q.popleft()
        for d in range(8):
            ni,nj = ci+di[d], cj+dj[d]
            # 탐색조건
            if 0<=ni<rows and 0<=nj<cols and worldmap[ni][nj]!='X' and dist[ni][nj]==0:
                #대각선 탐색 조건
                if d==1 and (worldmap[ci+1][cj]=='X' or worldmap[ci][cj+1]=='X'):   # 우측 하단
                    continue
                elif d==3 and (worldmap[ci][cj-1]=='X' or worldmap[ci+1][cj]=='X'): # 좌측 하단
                    continue
                elif d==5 and (worldmap[ci][cj-1]=='X' or worldmap[ci-1][cj]=='X'): # 좌측 상단
                    continue
                elif d==7 and (worldmap[ci-1][cj]=='X' or worldmap[ci][cj+1]=='X'): # 우측 상단
                    continue

                q.append((ni,nj))
                dist[ni][nj] = dist[ci][cj]+1
    # 지도의 가장 끝에 도달 못하는 경우는 없음!
    answer = dist[rows-1][cols-1]
    return answer