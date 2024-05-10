'''

N개 로프 -> k개 로프로 w인 물체 들기

들어올릴 수 있는 물체의 최대 중량
A  B
3 3 5 7 14 15

15 + 15 = 30/2 = 15
15 + 14 = 29/2 = 14.5

어차피 13, 15 있으면 무조건 13, 13까지만 가능함...

3 3 3 3 3 3 = 18
5 5 5 5     = 20
7 7 7       = 21
14 14       = 28
15          = 15
정답: 28!!
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())

arr.sort()
ans = arr[0]*n  # 최대 중량
for i in range(1,n):
    if arr[i-1] == arr[i]: continue
    ans = max(arr[i]*(n-i),ans)
print(ans)