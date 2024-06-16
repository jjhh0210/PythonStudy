'''
- a-b>=m 을 만족하는 a-b 중 최소값

<input>
3 3     # N, M
1       # 수열 시작
5
3
->4

5 6
2
3
9
13
22
ㅡㅡㅡㅡㅡㅡㅡ
- 중복해서 뽑을 수 있음!! a-a 이런식으로
'''

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
a = [0]*n
for i in range(n):
    a[i]=int(input())

## 투포인터 풀이 -> l,r 움직이는 거리 최대 2n->O(N)
a.sort()
l,r=0,0
ans = a[-1]-a[0]
while l<=r and 0<=l<n and 0<=r<n:
    diff = a[r]-a[l]
    if diff<m:
        r+=1
    elif diff>m:
        ans=min(ans, diff)
        l+=1
    else:   ## 같은경우
        ans=m
        break
print(ans)
