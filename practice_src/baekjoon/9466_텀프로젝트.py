'''
# 1차시도: 실패.. 너무 어려움
방향그래프에서 사이클 이루는/이루지 않는 정점 찾아내기
인접 행렬은 그래프에 간선이 많이 존재하는 밀집그래프
인접 리스트는 간선이 적은 희소그래프일 경우 사용

2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8
'''
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())    # 노드(정점) 개수
    arr = list(map(int, input().split()))
    # 인접 리스트 만들기 (1~)
    adj = [[] for _ in range(n+1)]
    for s,e in enumerate(arr):
        adj[s+1].append(e)

    #













