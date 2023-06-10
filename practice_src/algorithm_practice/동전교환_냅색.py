n = int(input())
coins = list(map(int, input().split()))
change = int(input())

dy = [500]*(change+1) # 거스름돈 j일때 최소 동전개수 (1<=m<=500)
dy[0] = 0

for coin in coins:
    for j in range(coin,change+1):
        dy[j] = min(dy[j], dy[j-coin]+1)

print(dy[change])