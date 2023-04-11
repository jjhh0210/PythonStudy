from collections import deque
# 1번 노드 -> 5번 노드 경우의 수
n,m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
ch = [0]*(n+1)  #체크배열
cnt = 0
ch[1] = 1   # 탐색시작 노드 초기화 (dfs(1)로 시작할거기때문)
path = deque()   # 경로 담을 리스트
def dfs(v):
    global cnt
    if v==n:    #도착지점 오면
        cnt+=1
        # for x in path:
        #     print(x,end=" ")
        print(*path)
    else:
        for i in range(1,n+1):
            if ch[i]==0 and g[v][i]==1:    # 체크돼있지 않고 인접행렬인 노드만 탐색
                ch[i] = 1
                path.append(i)
                dfs(i)
                path.pop()
                ch[i] = 0

for i in range(m):
    a,b = map(int, input().split())
    g[a][b] = 1

dfs(1)  #노드 1부터 탐색 시작!!
print(cnt)