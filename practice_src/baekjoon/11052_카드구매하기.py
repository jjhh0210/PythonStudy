n = int(input())
P = [0] + list(map(int, input().split()))

dp = [0] * (n+1)    # dp[i] = i개 구매하는 방법 중 최대 금액!!
# 4개 구매 최대 금액 : dp[4] = 1~4개팩 하나 구매(P[j]) + 나머지 남은 카드 개수 구하는 방법 중 최대금액(dp[4-j])
for i in range(1,n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+P[j])    # dp[4] = 3개구매하는방법중max + 1개팩구매, 2개구매하는방법중max + 2개팩구매, 1개팩구매방법중max + 3개팩, 4개팩구매 

print(dp[n])
