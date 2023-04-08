import sys
n, k = map(int,sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

# 처음 시작할 동전 구하기
# idx = 0
# for i in range(n-1,0,-1):
#     if coins[i] <= k:
#         idx = i
#         break

# 생각해보니 굳이 처음 시작할 동전을 안 구해도 된다... 효율만 더 안좋음
idx = len(coins)-1
cnt = 0
while k>0:      #k>=0으로 하면 이미 money는 0이 됐는데 coins 끝까지 다 돎
    a = k//coins[idx] # 동전 개수 더하기
    cnt+= a
    k = k%coins[idx]  # 그 동전으로 지불하고 남은 나머지 (만약 몫이0이면 안나눠졌다는 것이니까 k가 그대로겠지?)
    # print(coins[idx],"x",a, k)
    idx-=1

print(cnt)
