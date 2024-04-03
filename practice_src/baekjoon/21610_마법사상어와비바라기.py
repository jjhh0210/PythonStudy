
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
maps = [ list(map(int, input().split())) for _ in range(n)]
dps = [ tuple(map(int, input().split())) for _ in range(m)] # 이동규칙 집합

tainted = [[False]*n for _ in range(n)]  # 영양제 맞은 여부 배열
q = deque() # 영양제 좌표들
# di = [0,0,-1,-1,-1, 0, 1,1,1] # 코드트리) 방향배열 반시계(1~8 쓸거임!!), 대각선: 2,4,6,8
# dj = [0,1, 1, 0,-1,-1,-1,0,1]
di = [0, 0,-1,-1,-1,0,1,1,1] # 백준) 방향배열 시계(1~8 쓸거임!!), 대각선: 2,4,6,8
dj = [0,-1,-1, 0, 1,1,1,0,-1]

# 0. 초기 영양제 올려두기 in 좌하단 4칸
q.extend([(n-2,0),(n-2,1),(n-1,0),(n-1,1)])
for d,p in dps:
    # 1. 영양제 이동
    for _ in range(len(q)):
        ci,cj = q.popleft()
        ni,nj = (ci+di[d]*p)%n, (cj+dj[d]*p)%n  # 확인 필요! 순환 인덱스
        # 2. 영양제 투여 -> 높이+1
        maps[ni][nj]+=1
        tainted[ni][nj]=True    # 영양제 투여 표시
        q.append((ni,nj))
    
    # 3. 대각 성장
    while q:
        ci,cj = q.popleft()
        for dia_d in [2,4,6,8]:
            ni,nj = ci+di[dia_d], cj+dj[dia_d]
            # 대각선 애들 중 높이가 1이상이고, 범위 안에 들어가면 현재 높이 1씩 성장!
            if 0<=ni<n and 0<=nj<n and maps[ni][nj]>=1:
                maps[ci][cj]+=1
    # 4. 탐색하며 높이-2, 영양제 올리기
    for i in range(n):
        for j in range(n):
            # tainted가 아니고, 높이가 2이상이면 수행
            if not tainted[i][j] and maps[i][j]>=2:
                maps[i][j]-=2
                q.append((i,j)) # 영양제 투여하는게 아니므로 tainted는 XXX
            # 이제 올해 tainted인 애들은 내년을 위해 풀어주기!!
            if tainted[i][j]:
                tainted[i][j]=False

# 5. 다 끝나고 난 뒤 남아있는 높이들의 총 합 구하기
ans = sum(sum(row) for row in maps)
print(ans)


'''
코드트리 - 나무타이쿤

<조건>
- nxn
- 서로 다른 높이의 리브로수가 있음.
- 특수영양제: 리브로수 높이 1 증가 (씨앗 높이는 0->1이 됨)
- 초기에는 좌하단 4개칸에 영양제!
- 영양제 이동규칙 (이동 방향, 이동 칸 수)
- 이동 방향-> 1:오른쪽 ~ 8 //반시계로 8개 방향
    - 영양제 이동시 격자 밖으로 나가면 지구가 둥글듯 반대편으로 돌아옴⭐

1년⭐!!동안 성장 단계
1. 이동)
    특수영양제 규칙에 따라 이동시킴
    - 영양제 이동시 격자 밖으로 나가면 지구가 둥글듯 반대편으로 돌아옴⭐
2. 높이+1)
    해당 땅에 영양제 투여
3. 조건체크 개수cnt->높이+cnt)
    특수 영양제를 투입한 리브로수의 대각선으로 인접한 방향에
    높이가 1 이상인 리브로수가 있는 만큼 높이가 더 성장합니다.
    - 대각선으로 인접한 방향이 격자를 벗어나는 경우에는 세지 않습니다.!!!!!⭐
4. 조건체크 하면서 높이-2 -> 거기 영양제 체크)
    특수 영양제를 투입한 리브로수를 제외하고!!!!⭐️
    높이가 2 이상인 리브로수는 높이 2만큼을 자르고, 해당 위치에 특수 영양제를 올려둡니다.

다음년도로 올라가면 위 4단계 반복!!!⭐

<input>
5 5         # 격자 수n (3~15), 키우는 총 년수m (1~100)
1 0 0 4 2
2 1 3 2 1
0 0 0 2 5
1 0 0 0 3
1 2 1 3 3
1 3        # m개 줄 -> 각 년도의 이동 규칙 (1년차,2년차...m년차)
2 4        # 이동방향d(1~8), 이동칸수 p (1 ~ min(격자수,10)) 지구 두바퀴 돌일 없다!는뜻
7 1
5 2
4 1

<output>
m년 이후 남아있는 리브로수의 총 높이의 합
'''

