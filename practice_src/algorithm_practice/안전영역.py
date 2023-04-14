from collections import deque
import copy
n = int(input())
mapp = [list(map(int,input().split())) for _ in range(n)]
dq = deque()
dx = [-1,0,1,0]
dy = [0,1,0,-1]
#1. 높이 최댓값 찾기, 최솟값 찾기
maxx = max(map(max,mapp))
minn = min(map(min,mapp))

def bfs(m,rain):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if m[i][j] >= rain:
                cnt+=1
                m[i][j] == 0    # 비는 1~n높이까지만 올수있따
                dq.append((i,j))
                while dq:
                    now = dq.popleft()
                    for k in range(4):
                        nx = now[0]+dx[k]
                        ny = now[1]+dy[k]
                        if 0<=nx<n and 0<=ny<n and m[nx][ny] >= rain :
                            m[nx][ny] = 0
                            dq.append((nx,ny))

    return cnt

#2. 최소<=비높이<최대
ans = 0     #(비높이 = 지역최대높이 일경우 안전영역없음 ->0이 가장 최소개수)
for rain in range(minn,maxx):
    tmp_map = copy.deepcopy(mapp)
    range_num = bfs(tmp_map,rain)
    print(f"rain = {rain}, range_num = {range_num}")
    ans= max(ans,range_num)
print(ans)



