from collections import deque
n,m = map(int, input().split()) # 스타트, 목표
MAX = 100000
ch = [0]*(MAX+1)    #좌표는 0~100000까지
dis = [0]*(MAX+1)

#루트 노드 초기화
ch[n] = 1   # 해당 좌표 방문했는지
dis[n] = 0  # start에서 해당 좌표까지의 최단 거리
dq = deque()
dq.append(n)

def BFS(m) :
    if n == m:  #같은 지점의 경우 0초로 예외처리 필수!
        return 0
    while dq:  # 큐가 비어있지 않다면 (큐가 비어있을때까지 탐색)
        now = dq.popleft()
        for next in (now * 2, now + 1, now -1):
            if next ==m:  ## 만약 같아지면 return
                dis[next] = dis[now] + 1
                return
            if 0 <= next <= MAX and ch[next] == 0:
                ch[next] = 1
                dis[next] = dis[now] + 1
                dq.append(next)
BFS(m)
print(dis[m])