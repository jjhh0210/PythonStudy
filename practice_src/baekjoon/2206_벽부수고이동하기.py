'''
##1차시도: 실패
- 실패 원인
    - 2차원 배열로 시도함... 그러나 3차원 배열로 [안부수고 여기까지 온 경로, 한번 부수고 여기까지 온 경로] 따로 구분해줘야함
    - (i,j)까지 벽을 한 번도 부수지 않고 최단경로의 길이가 A, 벽을 한번 부수고 간 최단경로의 길이가 B이며 B<A인 경우,
        참고) https://www.acmicpc.net/board/view/90597
        2차원 배열 visited에는 벽을 부수고 간 최단경로 B만 저장됩니다.
        그러나 (i,j)를 지난 이후에 벽을 부수는 경로를 계산할 때에는 A로 계산을 해야 하나, 저장되어있던 B로 잘못 계산이 되는 상황이 발생하게 됩니다.
        정리하자면 (i,j)까지 벽을 부순 경로가 최단거리가 되어도, (n,m)까지의 최단경로는 (I,j)까지 벽을 부수지 않고 통과할 수도 있다는 것입니다.
- 2차원배열로 풀었을 때, 반례 케이스
9 9
010001000
010101010
010101010
010101010
010101010
010101010
010101010
010101011
000100010
정답: 33
- 2층으로 올라가면 다시는 1층으로 내려올 수 없음..!! 따라서 1층, 2층 (한번 부쉈는지, 안부쉈는지) 경로 따로 구분해야함,
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
mapp = [ list(map(int,list(input().rstrip('\n')))) for _ in range(n)]
# 3차원 배열!! dist[1][1][0 or 1] = 벽 안 부수고 온 거리, 벽 부수고 온거리
dist = [[[0]*2 for _ in range(m)] for _ in range(n)]
di = [-1,0,1,0] # 아래 왼 위 오(반시계)
dj = [0,-1,0,1]
q = deque()
# 초기화
q.append((0,0,0)) # (좌표, 부쉈는지) -> 안부숨 0, 부숨 1
dist[0][0][0]=1

ans=-1
# BFS
while(q):
    ci,cj,cwall = q.popleft()   # current (i,j,부숨 or 안부숨)
    if ci==n-1 and cj==m-1:
        ans=dist[n-1][m-1][cwall]
        break
    for d in range(4):
        ni,nj = ci+di[d], cj+dj[d]
        # OOR이 아니고,이전에 벽 부숨/안부숨 상태 기준으로 방문한 적 없고,벽이 아니거나 벽인데 부술수 있음 -> 탐색가능
        if 0<=ni<n and 0<=nj<m and dist[ni][nj][cwall]==0:
            # 벽이 아님 -> 탐색 가능
            if mapp[ni][nj]==0:
                q.append((ni,nj,cwall))
                dist[ni][nj][cwall]= dist[ci][cj][cwall]+1
            # 벽인데, 이때까지 안부셔서 한 번 부수기 가능
            elif mapp[ni][nj]==1 and cwall==0:
                q.append((ni,nj,1))
                dist[ni][nj][1] = dist[ci][cj][0]+1

# for a in dist:
#     print(*a)
print(ans)