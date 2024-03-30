
def move(ci,cj,di,dj):

    return ci,cj
def dfs(ri,rj,bi,bj,cnt):
    # 두개 위치 다르고, R이 exit인 경우
    global N,M,ans
    if maps[ri][rj]=='O':
        ans = cnt
        return
    # 탐색 시작
    for di, dj in dirs:
        # 1. 사탕 옮기기
        # 1-1) 탐색할 방향 기준 앞서있는 사탕 먼저 옮기기



        # 2. 둘다 exit이면 탐색X
        # 3. 다음 방향 호출



import sys
input = sys.stdin.readline

N,M = map(int, input().split())
maps = [ input().strip() for _ in range(N)]

dirs = [(-1,0), (1,0), (0,-1), (0,1)]  # 위, 아래 , 왼, 오
ri,rj,bi,bj = 0,0,0,0
ans=0
# 최초 사탕 위치 찾기
for i in range(1,N):
    for j in range(1,M):
        if maps[i][j] == 'R':
            ri,rj = i,j
        if maps[i][j] == 'B':
            bi,bj = i,j

dfs(ri,rj,bi,bj, 0)

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