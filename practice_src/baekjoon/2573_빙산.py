
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
mapp = [ list(map(int, input().split())) for _ in range(n)] #빙산
di,dj = [-1,0,1,0], [0,1,0,-1]

def bfs(n,m):
    # 1. 빙산이 다 녹은 상태인지 확인
    total_ice = sum([element for row in mapp for element in row])
    if total_ice==0:
        return 0

    # 2. 빙산 칸 탐색
    q = deque()
    visited = [[False]*m for _ in range(n)]
    ice_groups = 0      # 빙산 덩어리 개수
    decrease_ice = []   # 탐색 후 한번에 빙하 다 녹여야 함 (녹일 좌표, 녹일 수)
    for i in range(n-1):
        for j in range(m-1):
            if mapp[i][j] > 0 and not visited[i][j]:    # 빙산이면서, 방문한 적 없음
                if ice_groups==0:        # 빙산 탐색한 적 x(빙산 첫 탐색)
                    q.append((i,j))
                    visited[i][j]=True
                    ice_groups = 1     # 빙산 탐색함~
                    while q:
                        ci,cj = q.popleft()
                        cnt = 0 # 현재 칸의 주변 바다 개수
                        for d in range(4):
                            ni,nj = ci+di[d], cj+dj[d]
                            # 바다인 경우
                            if mapp[ni][nj]==0:
                                cnt+=1
                            # 빙산인 경우(방문한 적 없어야)
                            else:
                                if not visited[ni][nj]:
                                    q.append((ni,nj))
                                    visited[ni][nj]=True

                        decrease_ice.append((ci,cj,cnt))

                else:   # 한번 다 탐색했는데 아직 탐색 할 게 남아있다? 그럼 덩어리 생긴 것!
                    return 2    # 빙산 두개 발생

    # 3. 빙산 한번에 다 녹임
    for i,j,cnt in decrease_ice:
        mapp[i][j] = max(0, mapp[i][j]-cnt)

    return 1    # 빙산 크랙 발생 x


year = 0   # 햇수(년 단위)

while True:
    ice_groups = bfs(n,m)  # 0: 다 녹음, 1: 1개 덩어리(정상)  2: 2개 덩어리 발생
    if ice_groups==2:    # 멀티 덩어리 발견 돼서 중간에 종료
        break
    elif ice_groups==0: # 싱글 덩어리인 채로 빙하 다 녹아서 종료
        year=0
        break
    year+=1

print(year)