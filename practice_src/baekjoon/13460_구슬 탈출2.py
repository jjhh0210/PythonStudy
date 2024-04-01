def select_first():

def move_candy(ci,cj,di,dj):

    return ci,cj
def dfs(ri,rj,bi,bj,cnt):




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

dfs(ri,rj,bi,bj, 0) # R위치, B위치, 이때까지 몇번 기울였는지

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