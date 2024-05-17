'''
- 날 별 주가 -> 최대 이익

<input>
3   # T
3   # 날의 수 N(2~1000000)
10 7 6  # N날 별 주가(1~10000)
3
3 5 9
5
1 1 3 1 2
<output>
0
10
5
-----------------
예)
3 5 9
  u u
삼 삼 팔
3 -> +6
5 -> +4
최대 이익 10

5 5 12 12 10 2 1 10


1 1 3 1 2
  0 2 -2 1

떨어지기 전에 팔면 됨

1 +2
1 +2
1 +1

dp -> 부분문제해로 전체문제해 (최부구)O, 재사용 가능 x(점화식x)
그리디 -> 부분문제해로 전체문제해 O, 각 단계에서 최적의 선택이 전체적으로 최적의 결과(?..)

'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    maxx = arr[-1]
    for i in range(N-2,-1,-1):
        # 작으면 이익 더하기
        # 크거나 같으면 maxx 갱신
        if arr[i]<maxx:
            total+=maxx-arr[i]
        else:
            maxx = arr[i]

    print(total)