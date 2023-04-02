n,m = map(int, input().split())
nums = list(map(int, input().split()))
sum = 0
cnt = 0 # 합이 m이 되는 경우의 수
lt = 0

for rt in range(0,n):
    sum+=nums[rt]
    if sum == m:
        cnt+=1
    while sum >= m:
        sum -= nums[lt]
        if sum == m:
            cnt+=1
        lt+=1

print(cnt)

