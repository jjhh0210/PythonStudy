'''
<조건>
- S = A[0] × B[0] + ... + A[N-1] × B[N-1]
- A만 재배열해서 최소 S값 만들기

<input>
5
1 1 1 6 0
2 7 8 3 1
(N,A,B 차례대로)

<output>
18

<풀이>
어쨌든 큰수일수록 작은수와 곱해져야 최소값이 됨!!
1 2 3 7 8 (B 오름차순 정렬)
6 1 1 1 0 (A 내림차순 정렬)

'''

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
ans = 0

for i in range(n):
    ans += a[i]*b[i]

print(ans)