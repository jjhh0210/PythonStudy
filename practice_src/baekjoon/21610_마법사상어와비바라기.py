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
    해당 땅에 영양제 투여 -> 투여 후 영양제는 사라짐
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
from collections import deque
import sys
input = sys.stdin.readline
# 0 1 2 3 4 5
n=6 # 개수
i=2 # 현재 인덱스
k=5 # 몇번이동할건지


print((i+k)%n)  # i에서부터 +k 이동

print((i-k)%n)  # i에서부터 -k 이동

print(k%n)  # 0에서부터 +k이동

print(-k%n) # 0에서부터 -k이동
