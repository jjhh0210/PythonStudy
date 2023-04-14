from collections import deque
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]    # 이차원배열

ch = [[0]*n for _ in range(n)]  # 이차원 visitied 체크 배열
dx = [-1,0,1,0]
dy = [0,1,0,-1]
sum = 0
dq = deque()

#루트 초기화
mid = n//2
ch[mid][mid] = 1
sum += a[mid][mid]
dq.append((mid,mid))
L = 0   # 레벨 = n//2 -1 까지만 탐색하면 자동으로 nxn의 마름모 완성!!

while True:
    if L==n//2:
        break
    size = len(dq)
    print(L, size)
    for i in range(size):   # 레벨 카운트를 위해서!! 레벨별로 탐색
        now = dq.popleft()
        for j in range(4):  # 현재로부터 4방향으로 자식 뻗어나감
            next_x = now[0] + dx[j]
            next_y = now[1] + dy[j]
            if ch[next_x][next_y] == 0: #방문 안했다면
                sum +=a[next_x][next_y]
                ch[next_x][next_y] = 1
                dq.append((next_x,next_y))

    L = L+1 # 레벨 탐색 끝남
    for x in ch:
        print(x)
print(sum)