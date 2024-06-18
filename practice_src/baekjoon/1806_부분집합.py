'''
- N 짜리 수열 -> 연속된 수 들의 부분합 중 그 합이 S 이상 되는 것 중 가장 짧은 것의 길이
'''
import sys
input = sys.stdin.readline

n,s = map(int, input().split())
a = list(map(int, input().split()))

l=0
summ = 0
ans = float("inf")

for r in range(n):
    summ += a[r]
    if summ>=s:
        ans = min(r-l+1,ans)
    # l이 움직이는 경우
    while l<n and summ>=s:
        summ-=a[l]
        ans = min(r-l+1,ans)
        l+=1
if ans == float("inf"):
    print("0")
else:
    print(ans)

'''
반례)
10 30
1 1 1 1 1 1 15 1 1 15
정답:4
'''