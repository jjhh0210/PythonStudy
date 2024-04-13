'''
move = [(-1,0), (0,1),(1,0),(-1,0)]
<조건>
- LXL 크기의 체스판, (1,1)시작⭐️
- 칸: 0빈칸, 1함정 , 2벽(체스 OOR도 벽)
- 기사: (r,c 좌측상단 기준 h x w 크기 직사각형, 체력k)
- 명령받으면 상하좌우 중 한칸 이동, 이동시 연쇄작용, 끝에 벽있으면 모두 이동 못함⭐️
    - 없어진 기사에게 명령 내리면 반응 x️️️⭐️⭐️

- 해당 기사 한칸⭐️ 이동 (연쇄 이동 -> 이동한 곳에 밀려난 기사내부 함정 개수만큼 체력깎임)
    - 밀려난 기사들 피해봄: 함정의 수만큼만 피해 (명령받은애는 피해 x, 함정 없으면 피해 x)
    - 피해를 받은 만큼 체력이 깎이게 되며,
    - 현재 체력 이상의 대미지를 받을 경우 기사는 체스판에서 사라지게 됩니다.
    - 기사들은 모두 밀린 이후에 대미지를 입게 됩니다⭐️
        - 벽에 막혀서 이동 못하면 대미지 x!!!⭐️)

 Q 번의 대결이 모두 끝난 후 생존한 기사들이 총 받은 대미지의 합

<input>
4 3 3       # L체스판크기,N기사개수,Q번대결(명령)
0 0 1 0     # 체스판 (0 빈칸, 1 함정, 2 벽)
0 0 1 0
1 1 0 1
0 0 2 0
# 1~N번 기사 정보 차례대로
1 2 2 1 5  # (r,c),h세로,w가로,k초기체력
2 1 2 1 1
3 2 1 2 3
# Q개 명령정보
1 2 # i번기사, d방향으로 한칸 이동(0~3:위, 오른, 아래, 왼//시계방향!!)
2 1
3 3
'''
def draw(arr):
    for a in arr:
        print(a)
    print()

import sys
from collections import deque
input = sys.stdin.readline

L,N,Q = map(int, input().split())
# (1,1)~(L,L) 이니까 그냥 외곽 벽으로 감싸기! OOR 신경 안써도 됨 이제~~
maps = [ [2]*(L+2) for _ in range(L+2)]    # 체스판 상태 (0빈칸, 1함정 2벽)
knights = [ [0]*(L+2) for _ in range(L+2)]   # 기사 표시
for i in range(1,L+1):
    maps[i][1:L+1] = list(map(int, input().split()))
pos = [(0,0)]*(N+1)   # (r, c)
length = [(0,0)]*(N+1)   # (h, w)
hp = [0]*(N+1)  #k
total_dmg = [0]*(N+1) # 입은 총 데미지
bombs = [0]*(N+1)   # 기사별 내부 함정 갯수

for i in range(1,N+1):
    r,c,h,w,k = map(int, input().split())
    pos[i] = (r,c)
    length[i] = (h,w)
    hp[i] = k
    # 지도에 기사들 그리면서 기사별 함정 갯수 업데이트
    for a in range(r, r+h):
        # knights[a][c:c+w] = [i]*w
        # knights[a][c:c+w].count(1)
        for b in range(c, c+w):
            knights[a][b] = i
            if maps[a][b] == 1:
                bombs[i]+=1


commands = [tuple(map(int, input().split())) for _ in range(Q)]
# 0~3:   0위,    1오른,  2아래,  3왼    //시계방향!!
di = [-1,0,1,0]
dj = [0,1,0,-1]

# ## 대결 시작!
for idx, d in commands:
    ### 1. 이동 가능한지  검사 (다음 칸들에 벽있으면 이동x/ 기사있으면 append, 이동 가능 / 빈칸이면 이동 가능 )
    # 이동 불가능한 경우 : 벽있어서 못밈, 해당 기사가 탈락 (hp ==0)
    if hp[idx] ==0: continue    # 해당 기사 탈락했으면 skip

    q = deque([idx]) # 이동 대상 for BFS
    move = []    # 이동 대상
    while q:
        cnum = q.popleft()
        move.append(cnum)
        ci, cj = pos[cnum]
        h,w = length[cnum]
        # 위로
        if d == 0:
            for nj in range(cj,cj+w):
                if maps[ci-1][nj] == 2:  # 벽 있음
                    q.clear()
                    move.clear()
                    break
                else:
                    if knights[ci-1][nj] > 0 and knights[ci-1][nj] not in q:   # 다른 기사 있음
                        q.append(knights[ci-1][nj])
        # 오른쪽으로
        elif d==1:
            for ni in range(ci,ci+h):
                if maps[ni][cj+w] == 2:  # 벽 있음
                    q.clear()
                    move.clear()
                    break
                else:
                    if knights[ni][cj+w] > 0 and knights[ni][cj+w] not in q:   # 다른 기사 있음
                        q.append(knights[ni][cj+w])
        # 아래로
        elif d==2:
            for nj in range(cj,cj+w):
                if maps[ci+h][nj] == 2:  # 벽 있음
                    q.clear()
                    move.clear()
                    break
                else:
                    if knights[ci+h][nj] > 0 and knights[ci+h][nj] not in q:   # 다른 기사 있음
                        q.append(knights[ci+h][nj])
        # 왼쪽으로
        elif d==3:
            for ni in range(ci,ci+h):
                if maps[ni][cj-1] == 2:  # 벽 있음
                    q.clear()
                    move.clear()
                    break
                else:
                    if knights[ni][cj-1] > 0 and knights[ni][cj-1] not in q:   # 다른 기사 있음
                        q.append(knights[ni][cj-1])



    if not move: continue #move가 비어있다면 다음단계로!

    # 2. 이동 가능하면 연쇄 이동 (불가능하면 continue)
    for num in move[::-1]:  # 거꾸로!!
        # 이동할 변 선택 범위 동안 2) 마킹 다시 표시, 2) 함정 갱신
        # 마지막에 pos[num] 갱신!!
        i,j = pos[num]
        h,w = length[num]
        # 위로
        if d == 0:
            for nj in range(j, j + w):
                # 해당 방향으로 한칸 전진하며 변에 마킹하는데, 함정 있으면 카운트 +1
                if maps[i - 1][nj] == 1:
                    bombs[num] +=1
                knights[i-1][nj] = num

                # 반대 변은 마킹 해제하면서, 함정 있으면 카운트 -1
                if maps[i+h-1][nj] == 1:
                    bombs[num]-=1
                knights[i+h-1][nj]=0
        # 오른쪽
        elif d == 1:
            for ni in range(i, i + h):
                # 해당 방향으로 한칸 전진하며 변에 마킹하는데, 함정 있으면 카운트 +1
                if maps[ni][j+w] == 1:
                    bombs[num] +=1
                knights[ni][j+w] = num

                # 반대 변은 마킹 해제하면서, 함정 있으면 카운트 -1
                if maps[ni][j] == 1:
                    bombs[num]-=1
                knights[ni][j]=0
        # 아래
        elif d == 2:
            for nj in range(j, j + w):
                # 해당 방향으로 한칸 전진하며 변에 마킹하는데, 함정 있으면 카운트 +1
                if maps[i+h][nj] == 1:
                    bombs[num] +=1
                knights[i+h][nj] = num

                # 반대 변은 마킹 해제하면서, 함정 있으면 카운트 -1
                if maps[i][nj] == 1:
                    bombs[num]-=1
                knights[i][nj]=0
        # 왼쪽
        elif d == 3:
            for ni in range(i, i + h):
                # 해당 방향으로 한칸 전진하며 변에 마킹하는데, 함정 있으면 카운트 +1
                if maps[ni][j - 1] == 1:
                    bombs[num] += 1
                knights[ni][j - 1] = num

                # 반대 변은 마킹 해제하면서, 함정 있으면 카운트 -1
                if maps[ni][j + w - 1] == 1:
                    bombs[num] -= 1
                knights[ni][j + w - 1] = 0

        pos[num] = (i+di[d], j+dj[d])

    # 3. 모든 이동 후 밀린 기사들 데미지 깍기 (맨 처음은 명령받은 기사니까 X, move[1:])
    for num in move[1:]:
        # 체력 깍기 hp - bomb , 토탈 받은 데미지 갱신
        # 탈락 처리
        if hp[num] - bombs[num]<=0:     # 탈락하면 hp, total_dmg 모두 0 , 마킹 다 빼주기!!
            hp[num] =0
            total_dmg[num] = 0
            i, j = pos[num]
            h,w = length[num]
            for i in range(i, i+h):
                knights[i][j:j+w] = [0]*w

        else:
            hp[num] -= bombs[num]
            total_dmg[num] +=bombs[num]

    # print(total_dmg)
    # draw(knights)

## 최종
print(sum(total_dmg))






