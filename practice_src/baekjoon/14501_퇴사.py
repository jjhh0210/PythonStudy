'''
오늘1일, N일동안 최대한 많은 상담, N+1일에 퇴사
Ti: 완료에 걸리는 기간, 현재+t[i]일부터 일 가능
Pi: 받을 수 있는 금액

n개 중 최대값 될 수 있는 경우 찾기 -> 최대값 출력
d[i]: i일 째 당시 최대 수익 (i일 포함 X)
-> 그러므로 퇴사하는 d[n+1]날에 정산해야함
ex) n=7이면, 8일째에 퇴사하므로 8일까지 최대 수익을 구해야 함(d[8])
그래야 7일날 있는 상담까지 포함해서 계산됨(7일 째에는 7일날 있는 상담을 고려 안하므로)
d[7]: max(d[5]+a[5], d[4]+a[4], ....)
'''

import sys
input = sys.stdin.readline

n = int(input())
t = [0]*n
p = [0]*n
for i in range(n):
    t[i],p[i] = map(int, input().split())

d = [0]*(n+1)
for i in range(1,n+1):
    for j in range(i-1,-1,-1):
        # j일째에서 상담기간 더했을 때 현재일(i)과 같거나 작으면 j 상담 채택(p[j])
        if j+t[j]<=i:
            d[i] = max(d[j]+p[j],d[i])
print(max(d))
# print(d)