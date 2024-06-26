'''
- bottom to top
1. 테이블 정의
dp[i번째 자리][오는 수 j(0~10)] = i번째 자리가 j수일 때 가능한 경우의수

ex)dp[3][5] = 5 _ _ 일 때 가능한 경우의수

경우의수
- 앞에 오는수가 0: 뒤에는 1개 (1)
- 앞에 오는수가 1~8: 뒤에는 2개 (앞에오는수-1 + 앞에오는수+1)
- 앞에 오는수가 9: 뒤에는 1개 (8)

2. 점화식 구하기
- 앞에 오는 수가 0이면: dp[i][0] = dp[i-1][1]
- 앞에 오는 수가 1~8: dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
- 앞에 오는 수가 9이면: dp[i][9] = dp[i-1][8]
'''

N = int(input())
dp = [[0]*10 for _ in range(N+1)]   # 0~9까지가 N개

# 1자리수일 때 초기화
for i in range(1,10):
    dp[1][i] = 1    # 한자리 수 일땐 1~9 경우의수 모두 1

# bottom up (2자리수~N자리수까지 채우기)
for i in range(2, N+1):
    for j in range(10):
        if j==0:
            dp[i][j] = dp[i-1][1]
        elif 1<=j<=8:
            dp[i][j] = dp[i-1][j-1]+ dp[i-1][j+1]
        else:

            dp[i][j] = dp[i-1][8]
for i in range(1,N+1):
    print("%d 자리수:" %i,end="")
    print(dp[i][:])
print(sum(dp[N])%1000000000)



