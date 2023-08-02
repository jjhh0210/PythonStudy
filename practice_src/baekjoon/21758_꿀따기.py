import sys
n = int(sys.stdin.readline().rstrip())
honeys = list(map(int, sys.stdin.readline().rstrip().split()))

## 꿀의 누적합 구하기
prefix_sum = [0]*n
prefix_sum[0] = honeys[0]
for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1]+honeys[i]

## 3가지 경우의 수
#1. 벌 벌 통
maxx = 0
for i in range(1,n-1):
    first_step = prefix_sum[n-1]-honeys[0]
    temp = first_step - honeys[i] + prefix_sum[n-1] - prefix_sum[i]
    maxx = max(maxx,temp)

#2. 벌 통 벌
for i in range(1, n-1):
    first_step = prefix_sum[n-2] - honeys[0] # 전체 합에서 양끝 제거
    temp = first_step+honeys[i]
    maxx = max(maxx,temp)


#3. 통 벌 벌
for i in range(1,n-1):
    first_step = prefix_sum[n-2]
    temp = first_step - honeys[i] + prefix_sum[i-1]
    maxx = max(maxx,temp)

print(maxx)


