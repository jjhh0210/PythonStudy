'''
- 1년 마다 동서남북 중 0의 개수만큼 줄어듦
- 빙산이 두덩어리 이상으로 분리되는 최초의 년을 구하라 (다 녹을 때까지 분리안되면 0)
- edge
n,m 3 ~ 300
빙하 최대 높이 10

# 1차시도 -> 실패
- 이유: 바다와 닿아 있지 않고 여러 겹의 빙하로 둘러싸인 빙하 칸은 녹을 수 있는 시점이 10년을 훌쩍 넘을 수도 있습니다.

# 2차시도 -> 파이썬은 시간초과 / pypy3은 통과
- 초과이유: 이중 for문 때문에... 최악의 경우 n,m=300일때 90000번 돌아야함. 근데 빙산은 10000개까지만 들어갈 수 있다고 문제에 나와있음!!
- 해결: 전체 mapp대신 빙산 좌표만 담은 list로 다시 구현해보자.
'''
import copy
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    # 가장 먼저 빙산인 곳 찾기
    global n,m,ices
    q = deque()
    temp_mapp = copy.deepcopy(mapp)
    next_ices= []
    visited = [[0]*m for _ in range(n)]
    flag = 0   # 빙산 탐색 시도 -> 0: 빙산 발견 못함, 1: 빙산 탐색함
    for i,j in ices:
        if temp_mapp[i][j] > 0 and visited[i][j]==0:    # 빙산이면서, 방문한 적 없음
            if flag==0:        # 빙산 탐색한 적 x(빙산 첫 탐색)
                q.append((i,j))
                visited[i][j]=1
                flag = 1     # 빙산 탐색함~
                while q:
                    ci,cj = q.popleft()
                    cnt = 0 # 현재 칸의 주변 바다 개수
                    for d in range(4):
                        ni,nj = ci+di[d], cj+dj[d]
                        # 바다인 경우
                        if temp_mapp[ni][nj]==0:
                            cnt+=1
                        # 빙산인 경우(방문한 적 없어야)
                        elif temp_mapp[ni][nj] > 0 and visited[ni][nj]==0:
                            q.append((ni,nj))
                            visited[ni][nj]=1
                    if mapp[ci][cj]-cnt>0:  # 녹았는데 여전히 빙산 (자연수)
                        mapp[ci][cj] = mapp[ci][cj]-cnt
                        next_ices.append((ci,cj))
                    else:                   # 녹아서 바다됨 (0)
                        mapp[ci][cj]=0
            else:   # 한번 탐색했는데 아직 mapp에 탐색 할 게 남아있다? 그럼 덩어리 생긴 것!
                return True    # 빙산 크랙 발생
    ices = next_ices
    return False    # 빙산 크랙 발생 x


n,m = map(int, input().split())
# mapp = [ list(map(int, input().split())) for _ in range(n)] #빙산
# 빙산칸 좌표
mapp = [[0]*m for _ in range(n)]
ices = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        mapp[i][j] = temp[j]
        if mapp[i][j] > 0:
            ices.append((i,j))    # 빙산칸 좌표

di,dj = [-1,0,1,0], [0,1,0,-1]

i = 0   # 횟수(년 단위)
iscracked = False    # 크랙 발생?
# 멀티 덩어리 발견 돼서 중간에 종료 / 싱글 덩어리인채로 빙하 다 녹아서 종료 -> 빙하 다 녹을 때 까지 돌리면 됨.
while ices:
    i+=1    # +1년
    iscracked = bfs()
    if iscracked:   # 올해의 빙하 탐색 중 크랙 발견함
        print(i-1)  # 작년에 녹은 결과로 이미 멀티 덩어리 생성된 것
else:
    print(0)