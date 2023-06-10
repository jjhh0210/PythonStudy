import sys
N, M = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10**7)        # 재귀 허용 범위 넓혀준다!(안하면 재귀제한 걸려서 넘어가면 런타임에러)
#인접리스트 - 인접행렬은 아무래도 시간효율이 매우 떨어짐
graph = [[] for _ in range(N+1)]
#인접행렬
for _ in range(M):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ch = [0]*(N+1)  #정점 방문여부 확인
cnt = 0
def dfs(v):
    for i in graph[v]:
        if ch[i]== 0:
            ch[i] = 1
            dfs(i)

for i in range(1,N+1):
    if ch[i]==0:
        cnt+=1
        dfs(i)

print(cnt)




