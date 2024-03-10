import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

d = [0]*n
d[0] = nums[0]

for i in range(1,n):
    maxx = 0
    for j in range(i-1,-1,-1):
        if nums[j]<nums[i]:
            maxx = max(maxx,d[j])
    d[i] = maxx + nums[i]
print(max(d))
# print(d)
