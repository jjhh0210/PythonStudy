def select_first(ri,rj,bi,bj,d):
    if d == 0:  # 위로 이동 -> i가 더 작은 것이 먼저 이동
        return 'R' if ri<bi else 'B'
    elif d==1:  # 아래 이동 -> i가 더 큰 것이 먼저 이동
        return 'R' if ri>bi else 'B'
    elif d == 2:  # 왼쪽 이동 -> j가 더 작은 것이 먼저 이동
        return 'R' if rj<bj else 'B'
    else:           # 오른쪽 이동 -> j가 더 큰 것이 먼저 이동
        return 'R' if rj>bj else 'B'

def move_candy(ci,cj,di,dj,moving_candy):
    # 4가지 경우 -> 빈칸 나옴 / exit이 나옴 / 벽이나 다른 사탕이 나옴 => 사탕 최종 위치 반환

    maps[ci][cj] = '.'  # 우선 현재 사탕 칸을 빈 칸으로 변경
    while True:
        if maps[ci + di][cj + dj] == '.':   # 빈칸이 나오면? : 움직이고 계속
            ci,cj = ci+di,cj+dj
            continue
        elif maps[ci+di][cj+dj]== 'O':      # exit이 나오면? : 움직이고 끝!! 사탕 표시 XX
            ci,cj = ci+di,cj+dj
            return ci,cj
        else:                               # 벽이나 다른 사탕이 나오면? : 안움직이고 끝
            break
    maps[ci][cj] = moving_candy # exit 아닌 경우, 최종 사탕 위치 표시
    return ci,cj


def dfs(ri,rj,bi,bj,cnt):
    global N,M,ans,maps

    ## 사탕들 exit여부 4가지 경우 중 두개 다 exit 아닌 경우에만 기울기 진행 가능!
    # 1)둘다 exit / 2) 빨강 X and 파랑 O -> return
    if (maps[ri][rj] == 'O' and maps[bi][bj] == 'O') or (maps[ri][rj] != 'O' and maps[bi][bj] == 'O'):
        return
    # 3) 빨 O 파 X -> 정답 상태 도달! answer 갱신, return
    if maps[ri][rj] == 'O' and maps[bi][bj]!='O':
        ans = min(cnt, ans) if ans!=-1 else cnt # ans가 -1이면 cnt가 ans, 아니면 기존보다 더 작은거
        return
    # 4) 둘 다 exit 아님 -> 기울기 진행
    ## 기울기 횟수 이미 10번을 채웠다면? return
    if cnt == 10:
        return
    for d in range(4):
        # 1. 해당 방향으로 사탕 옮길 수 있는지 확인 -> 사탕 둘 중 한개라도 '다음이 빈칸이거나 exit'을 충족하면 이동 수행 가능!!!
        di,dj = dirs[d][0], dirs[d][1]
        nri,nrj,nbi,nbj = ri+di,rj+dj,bi+di,bj+dj
        if maps[nri][nrj] == "." or maps[nri][nrj] == "O" or maps[nbi][nbj] == "." or maps[nbi][nbj] == "O":
            # 2. 해당 방향으로 사탕 두 개 옮기기
            # 2-1) 먼저 옮길 사탕 구하기
            first = select_first(ri,rj,bi,bj,d)
            # 2-2) 사탕 두개 옮기기 (기울기 끝난 상태 maps에 기록 / 최종 사탕 위치 반환)
            if first=='R':
                moved_ri, moved_rj = move_candy(ri,rj,di,dj,'R')
                moved_bi, moved_bj = move_candy(bi,bj,di,dj,'B')
            else:
                moved_bi, moved_bj = move_candy(bi,bj,di,dj,'B')
                moved_ri, moved_rj = move_candy(ri,rj,di,dj,'R')
            # 3. 다음 단계로 호출하기
            # 3-1) 호출
            dfs(moved_ri,moved_rj,moved_bi,moved_bj,cnt+1)
            # 3-2) 호출 전 상태로 map 되돌리기
            # - exit이 아닌 사탕 : 예전 위치에 R,B표시, 현재위치를 빈칸으로
            # - exit인 사탕 : 예전 위치에 R,B표시
            if maps[moved_ri][moved_rj] !='O':              # exit아닌 경우 현재 위치를 빈칸으로 되돌리기
                maps[moved_ri][moved_rj] = '.'
            if maps[moved_bi][moved_bj] !='O':
                maps[moved_bi][moved_bj] = '.'
            maps[ri][rj],maps[bi][bj] = 'R','B'             # 예전 위치에 다시 R,B표시 ( 이 두개 순서 바뀌면 안됨,,)

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
maps = [ list(input().strip()) for _ in range(N)]

dirs = [(-1,0), (1,0), (0,-1), (0,1)]  # 위, 아래 , 왼, 오
ri,rj,bi,bj = 0,0,0,0
ans=-1

# 최초 사탕 위치 찾기
for i in range(1,N):
    for j in range(1,M):
        if maps[i][j] == 'R':
            ri,rj = i,j
        if maps[i][j] == 'B':
            bi,bj = i,j


dfs(ri,rj,bi,bj, 0) # R위치, B위치, 이때까지 몇번 기울였는지
print(ans)
'''
코드트리- 2개의 사탕 / 2015년 하반기 삼성 그룹 오후 2번

## 조건 ##
- 빨간 사탕 꺼낼거임
- 기울이면, 장애물 / 다른 사탕 부딪히기 전까지 이동 (이동 도중 기울이기x)
- 한 step에서) 빨간 사탕만 무조건 먼저 나와야!!! 파란 사탕이 먼저 or 동시에 나오는거 x
빨간색 사탕 빼내기 위해 기울이는 최소 횟수 구하기!!1

## 입력 ##
N M (3~10, 3x3 ~ 10x10)
maps
- maps 공백없이 주어짐!!
- 상자 바깥부분 모두 장애물로 막아놓음

## 출력 ##
빨간색 사탕 빼내기 위해 기울이는 최소 횟수
- if 기울이는 최소 횟수 > 10 : -1
'''