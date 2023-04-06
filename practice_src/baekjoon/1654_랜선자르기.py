k,n = map(int, input().split())
lans = []
for _ in range(k):
    lans.append(int(input()))

# 갖고있는 k개의 랜선들 중 가장 큰 랜선 길이
# 가장 작은 랜선 길이로 하지 않는 이유는, 모든 k개의 랜선을 다 자를 필요가 없기 때문
# ex) lans = [100,1,1] 이고 n=2인 경우, 100을 두 개로만 자르면 됨
largest = max(lans)

# 1 ~ largest 중 n개로 자를 수 있는 최대 길이 구해야 by 이분탐색
lt = 1
rt = largest
res = 0
while lt<=rt:
    mid = (lt+rt)//2
    # 11개로 잘라지는지 확인
    summ = sum([x//mid for x in lans])
    # print(summ)
    if summ < n:
        rt = mid - 1
    elif summ >= n: # n이 되어도 mid 보다 더 큰 길이로도 나눠질 수도 있으니까 mid보다 큰 범위 더 탐색!
        res = mid # 답 갱신해놓음
        lt = mid + 1

print(res) # 결국은 최적의 해가 출력될 것!
# print(lt, rt, mid)