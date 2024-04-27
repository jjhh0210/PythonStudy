'''
1. 테이블 정의
d[i] = i번째 삼각형의 변의 길이

2. 점화식 구하기
d[i] = d[i-5]+d[i-1]   (i>=5)

3. 초기값
d[0,1,2,3,4] = [0,1,1,1,2]

'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    d = [0]*(N+1)
    d[:5] = [0,1,1,1,2] # d[0~4] 까지 초기값 설정
    for i in range(5,N+1):
        d[i] = d[i-5]+d[i-1]

    print(d[N])
