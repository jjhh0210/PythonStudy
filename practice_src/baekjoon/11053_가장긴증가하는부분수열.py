'''
10 20 10 30 20 50
1  2  1  3  2  4
'''

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = [1]*n   # i번째 항을 끝으로 하는 가장 긴 부분 수열 길이 -> 1부터 시작
for i in range(1,n):
    for j in range(i-1,-1,-1):
        if a[j]<a[i]:
            d[i] = max(d[j]+1,d[i])
print(max(d))
# print(d)


