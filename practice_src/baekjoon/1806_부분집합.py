'''
- N 짜리 수열 -> 연속된 수 들의 부분합 중 그 합이 S 이상 되는 것 중 가장 짧은 것의 길이
10 15
5 1 3 5 10 7 4 9 2 8
'''
import sys
input = sys.stdin.readline

n,s = map(int, input().split())
a = list(map(int, input().split()))

l=0
summ = 0
ans = n
# for r in range(n):
#     summ += a[r]
#     if summ>=s:
#         ans = min(r-l+1,ans)
#     # l이 움직이는 경우
#     while l<n and summ>s:
#         summ-=a[l]
#         l+=1
#     if summ>=s:
#         ans = min(r-l+1,ans)

r=0
while 0<=r<n and 0<=l<n:
    if summ>=s:
        ans = min(r-l,ans)
        summ-=a[l]
        l+=1
    else:
        summ+=a[r]
        r+=1

print(ans)