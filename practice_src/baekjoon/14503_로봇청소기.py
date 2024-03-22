# import sys
# input = sys.stdin.readline
#
# N,M = map(int,input().split())
# r,c,d = map(int,input().split())
# maps = [ list(map(int, input().split())) for _ in range(N)]
#
# di = [-1,0,1,0]
# dj = [0,1,0,-1]
#
# ans = 0
# while True:
#     if maps[r][c] == 0:
#         maps[r][c]=2
#         ans +=1
#     for _ in range(4):
#         d = (d-1)%4
#         nr,nc = r+di[d],c+dj[d]
#         if maps[nr][nc]==0:
#             r,c = nr, nc
#             break
#     else:
#         nr,nc = r-di[d],c-dj[d]
#         if maps[nr][nc]==1:  #벽이 아니어야 후진 가능
#             break
#         r,c = nr,nc
# print(ans)


import sys
input = sys.stdin.readline

N,M = map(int,input().split())
r,c,d = map(int,input().split())
maps = [ list(map(int, input().split())) for _ in range(N)]

move = [ [-1,0], [0,1], [1,0], [0,-1]]  #북 동 남 서
ans = 0
while True:
    if maps[r][c] == 0:
        maps[r][c]=4
        ans +=1
    for ni,nj in move:
        if maps[r+ni][c+nj]==0:
            d = (d-1)%4
            di,dj = move[d]
            if maps[r+di][c+dj] ==0:
                r,c = r+di, c+dj
            break
    else:
        di,dj = move[d]
        if maps[r-di][c-dj]!=1:  #벽이 아니어야 후진 가능
            r,c = r-di, c-dj
        else:   # 뒤가 벽이라 후진 못함 -> while 탈출
            break
print(ans)
'''
<input>
N M  (행 N 열 M --- 3<=N,M<=50)
r c d (청소기 현좌표 r c 방향 d --- d= 0북 1동 2남 3서)
maps (0 청소안된 빈칸, 1 벽)

<조건>
방 끝들은 다 벽
청소기는 무조건 빈칸에만 있음
벽 후진 못하면 작동 멈춤!!!!! break
----
'''
print(r,c,d)
for a in maps:
    print(a)

