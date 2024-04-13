'''
- M명의 참가자
- NxN 미로 , (1,1)부터⭐️
- 미로: 0빈칸, 1~9내구도 벽
    - 회전할 때, 내구도가 1씩 깎입니다.
    - 내구도가 0이 되면, 빈 칸으로 변경됩니다.
- 출구 도착시 참가자는 즉시 탈출

For K초
1. 1초마다 ⭐️모든 참가자 한 칸씩 동시에⭐️ 움직임
    - 상하좌우로 현재보다 출구까지 최단거리가 가까워지는⭐️ 곳인 빈칸으로 이동 가능!!!못움직이면 움직임x
        - 우선순위 : 출구와가까워지는 최단거리 -> 방향은 상하⭐️가 우선!!
        - 한 칸에 참가자 중복 가능!!
2. 이동 끝-> 미로 회전
    - (최소 1명 이상의 참가자 & 출구) 포함하는 가장 작은 ⭐️정사각형⭐️ 잡기
        - 우선순위: 크기 작음 -> 좌상단 r 작음 -> c 작음
    - 해당 정사각형 시계 90도 회전, 회전된 벽들은 내구도 -1씩

if K초 전에 모든 참가자 탈출 => 즉시 게임 끝

게임끝 -> 모든 참가자들의 이동 거리 합(총 이동 거리?횟수?) , 출구 좌표 출력

<인풋>
5 3 8       # N크기미로(1~10), M참가자수(1~10), K초
0 0 0 0 1
9 2 2 0 0
0 1 0 1 0
0 0 0 1 0
0 0 0 0 0
# M개의 참가자 좌표(초기에 빈칸에만 존재)
1 3
3 1
3 5
# 초기 출구 좌표
3 3

'''
from collections import Counter
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

pos= Counter()
# 참가자 좌표
for _ in range(M):
    i, j = map(lambda x: int(x) - 1, input().split())
    pos.update([(i, j)])

# 출구 좌표
exi, exj = map(lambda x: int(x) - 1, input().split())

di = [1, -1, 0, 0]  # 상 하 좌 우
dj = [0, 0, -1, 1]
ans = 0
# K초 동안
for _ in range(K):
    '''
    1. 1초마다 ⭐️모든 참가자 한 칸씩 동시에⭐️ 움직임
    - 상하좌우로 현재보다 출구까지 최단거리가 가까워지는⭐️ 곳인 빈칸으로 이동 가능!!!못움직이면 움직임x
        - 우선순위 : 출구와가까워지는 최단거리 -> 방향은 상하⭐️가 우선!!
        - 한 칸에 참가자 중복 가능!!
2. 이동 끝-> 미로 회전
    - (최소 1명 이상의 참가자 & 출구) 포함하는 가장 작은 ⭐️정사각형⭐️ 잡기
        - 우선순위: 크기 작음 -> 좌상단 r 작음 -> c 작음
    - 해당 정사각형 시계 90도 회전, 회전된 벽들은 내구도 -1씩

if K초 전에 모든 참가자 탈출 => 즉시 게임 끝
    '''
    # 모두 탈출했다면 break
    if not pos:  # pos가 비었다면?
        break

    ## 1. 참가자 한칸 씩 이동
    moved = Counter() # 움직인 애들 좌표
    arr = list(pos.keys())
    for ci, cj in arr:
        min_dist = 2*N
        i,j = ci,cj     # 움직일 최종 좌표
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            dist = abs(ci-exi) + abs(cj-exj)
            # 움직일 수 있는 조건: OOR 아니고, 빈칸이나 사람 있어야 하고, 최단 거리 갱신되어야 하고
            if 0<=ni<N and 0<=nj<N and maps[ni][nj] ==0 and dist<min_dist:
                min_dist = dist
                i,j = ni,nj
        # 이동 할 수 있으면 이동
        if (i,j) != ci,cj:
            ans += pos[(ci, cj)]  # 해당 좌표 애들 다 움직임
            moved[(i, j)] += pos[(ci, cj)]
            pos.pop((ci, cj))  # 움직여서 이제 없음

    # 움직이지 않은 애들이랑 움직인 애들 좌표 합치기!!
    pos.update(moved)

    # 사람 표시하기
    for (i,j) in pos:
        maps[i][j] = -pos[(i,j)]

    ## 2. 미로 회전
    # 1) 정사각형 잡기 (벽돌 -1)
    # - 최소 변의 길이 정하기 (+ 반드시 포함할 애 선정)
    min_w = N
    ti, tj = N, N
    for ci,cj in pos:
        # 가로, 세로 중 큰게 변의 길이
        w = max(abs(ci-exi),abs(cj-exj))+1
        if (min_w,ti,tj) > (w, ci,cj):
            # 반드시 포함할 애 갱신
            min_w, ti, tj = w, ci,cj
    # - 좌측상단 시작점 si, sj 정하기
    endi = max(ti, exi)
    endj = max(tj, exj)
    si = 0 if endi - w + 1 < 0 else endi - w + 1
    sj = 0 if endj - w + 1 < 0 else endj - w + 1

    # 정사각형 부분 회전
    matrix = [row[sj:sj+w] for row in maps[si:si+w]]
    # 매트릭스안에 있는 벽 깎고,
    for i in range(w):
        for j in range(w):
            if matrix[i][j]>0:
                matrix[i][j] -=1

    matrix = list(map(list, zip(*matrix[::-1])))
    # 벽 깎고,






