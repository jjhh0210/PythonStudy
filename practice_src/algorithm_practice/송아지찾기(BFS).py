from collections import deque
n,m = map(int, input().split()) # 스타트, 목표
MAX = 10000
ch = [0]*(MAX+1)    #좌표는 1~10000까지
dis = [0]*(MAX+1)

#루트 노드 초기화
ch[n] = 1   # 해당 좌표 방문했는지
dis[n] = 0  # start에서 해당 좌표까지의 최단 거리
dq = deque()
dq.append(n)

def BFS(m,ch,dis,dq) :
    while dq:  # 큐가 비어있지 않다면 (큐가 비어있을때까지 탐색)
        now = dq.popleft()
        # if now ==m:   # 이렇게 보다는 자식에서 바로 return 하는게 나음
        #     break
        for next in (now - 1, now + 1, now + 5):
            if next == m:
                dis[next] = dis[now] + 1
                return
            if 0 < next <= MAX and ch[next] == 0:
                ch[next] = 1
                dis[next] = dis[now] + 1
                dq.append(next)

BFS(m,ch,dis,dq)
print(dis[m])