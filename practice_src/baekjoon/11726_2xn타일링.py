import sys, math
input = sys.stdin.readline

n = int(input())
# a = n//2   # 2의 개수
# sum = 0
# for i in range(a+1):    #2의 개수가 0~n까지 각각 경우의수
#     sum+= math.comb(n-i,n-2*i)
# print(sum%10007)

'''DP로 해결'''
d = [0]*1001
d[1], d[2] = 1,2
for i in range(3,n+1):
    d[i] = (d[i-1] + d[i-2])%10007
print(d[n])
