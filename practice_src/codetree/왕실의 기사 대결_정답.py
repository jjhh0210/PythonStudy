'''
<조건>
- 정답: 초기 체력 합 - 현재 체력 합 = 이때 까지 받은 총 데미지!!
- 탈락이 있으므로, 기사번호 별 info를 여러개 관리해야 하므로 딕셔너리 쓰자!

maps = [][] # 체스판
v = [][]# 디버그용

units = {1 : [i,j,h,w,k]
         2 : [i,j,h,w,k]}

init_k = [] # 초기 데미지
dmgs = []   # 기사 별 안에 있는 함정들 (줄 피해)

<겹치는거 확인할 때 다른 방법)
# ### 하드코딩 방법: 네 변에 대해 s < te OR ts<e 체크!!!
#     #상 하 / 좌 우
# if ((ni==ti+th-1 or ni+h-1==ti) and (tj<=nj<tj+tw or tj<=nj+w-1<tj+tw or nj<=tj<nj+w or nj<=tj+tw-1<nj+w)) \
#         or \
#     ((nj==tj+tw-1 or nj+w-1==tj) and (ti<=ni<ti+th or ti<=ni+h-1<ti+th or ni<=ti<ni+h or ni<=ti+th-1<ni+h)):
#     q.append(idx)
#     move.add(idx)
'''
import sys
from collections import deque
input = sys.stdin.readline

#방향: 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [ 0, 1, 0,-1]

N,M,Q = map(int, input().split())
maps = [[2]*(N+2)]+[[2]+list(map(int, input().split()))+[2] for _ in range(N)]+[[2]*(N+2)]
units = {}
# v = [[0]*(N+2) for _ in range(N+2)] # 디버거로 동작확인용
init_k = [0]*(M+1)

for m in range(1,M+1):
    si,sj,h,w,k = map(int,input().split())
    units[m] = [si,sj,h,w,k]
    init_k[m] = k
    # for i in range(si,si+h):
    #     v[i][sj:sj+w] = [m]*w


# 나는 탐색 시간 줄이겠다고 이동 방향으로의 변만 탐색하고 갱신하면서 움직였는데...
# 이 코드는 그냥 push할 때마다 해당 기사 영역 새로 탐색+ 함정 새로 카운트
# 근데도 시간 똑같이 걸림
def push_units(start, d):  # start기사번호, 움직일방향
    # start를 밀면서 연쇄처리, 중간에 벽 만나면 아묻따 return
    q = deque([start]) # 이동 후보 탐색용
    move = set([start]) # 실제로 이동할 대상
    damage = [0]*(M+1) # 함정 개수

    ## 1. 우선 내가 이동 할 영역 모두 탐색!
    while q:
        num = q.popleft()
        ci,cj,h,w,k = units[num]
        ni,nj = ci+di[d], cj+dj[d]
        # 벽/함정: 이동할 곳 안에 벽 있으면 return / 함정 잇으면 카운트
        for i in range(ni,ni+h):
            for j in range(nj,nj+w):
                if maps[i][j] == 2:  # 벽이 잇다면 바로 return
                    return
                if maps[i][j] == 1:  # 함정 있으면 추가!
                    damage[num] +=1

        # 나랑 겹치는 기사 있을지 확인(모든 기사 체크): q, move에 추가
        # 방향이 어떻던 간에 겹치는 애들 있으면 : 밀림의 대상
        for idx in units:
            if idx not in move:
                ti, tj, th,tw,tk = units[idx]
                # ⭐️겹치는 경우) t의 시작점범위: 내끝부터 위로, 끝점 범위: 내 시작부터 아래로 (굿노트참고)
                # t의 시작/ 끝 : ti, tj / ti+th-1 ,tj+tw-1
                if ti <= ni+h-1 and tj <=nj+w-1 and ti+th-1 >=ni and tj+tw-1 >= nj:
                    q.append(idx)
                    move.add(idx)

    # 명령 받은 기사는 데미지 입지 않음 -> 함정 없애기
    damage[start] = 0

    ## 2. 실제로 기사들 이동하면서 체력 깎기 (데미지>=체력 시 기사는 탈락)
    for idx in move:
        si,sj,h,w,k = units[idx]

        if k<=damage[idx]:  # 체력보다 더 큰 데미지면 삭제
            units.pop(idx)
        else:
            ni,nj=si+di[d], sj+dj[d]
            units[idx]=[ni,nj,h,w,k-damage[idx]]    # 기사 정보 갱신
# 명령 수행 (밀기 -> 데미지 처리하기)
for _ in range(Q):
    idx, dr = map(int, input().split())
    # 탈락 안한 애들이면 일단 명령 수행 해봄
    if idx in units:
        push_units(idx, dr) # # 명령받은 기사(연쇄적으로 밀기! 벽이 없는 경우)

# 총 데미지 추출
ans = 0
for idx in units:
    ans+= init_k[idx] - units[idx][4] # 초기 체력 - 현재 체력
print(ans)
