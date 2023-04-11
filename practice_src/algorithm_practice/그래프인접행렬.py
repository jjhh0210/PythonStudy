n,m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)] #0~n까지 배열이 0~n개 (2차원배열)

#인접행렬 만들기
for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 인접행렬 출력
for i in range(len(graph)):
    for j in range(len(graph[i])):
        print(graph[i][j],end=' ')
    print()