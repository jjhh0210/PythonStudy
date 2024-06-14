'''
- (A - B)의 모든 원소를 구하라 (A에만 있고 B에는 없는)
- 한 집합에 속하는 모든 원소의 값은 다르다(중복 없음) -> set 이용 가능!!

<in>
4 3         #n(A), n(B)
2 5 11 7    # A
9 7 4       # B
<out>
3           # A-B개수 (없으면 0)
2 5 11      # 원소
'''

import sys
input = sys.stdin.readline

na,nb = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

ans = a-b
ans = sorted(ans)
print(len(ans))
if ans:
    print(*ans)
