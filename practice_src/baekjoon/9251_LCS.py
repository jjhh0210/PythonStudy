'''

LCS: 최장공통부분수열, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾기

1. 테이블 정의
LCS[i][j] = a문자열에서 i번째가 끝이고, b문자열에서 j번째가 끝인 문자열의 LCS

2. 점화식 정의

if 끝 두개가 같을 때 : LCS[i-1][j-1] + 1   # 맨마지막 문자 뺐을 때 애들의 LCS에서 1을 더해줌! (갱신)
if 끝 두개가 다를 때: max(LCS[i-1][j],LCS[i][j-1]) # a의 맨 마지막 없을 때의 LCS, b의 맨 마지막 없을 때의 LCS 중 큰거 그대로 (유지)

3. 초기값 설정
i-1, j-1을 쓰기 때문에 LCS 에서 문자열 시작 인덱스를 1부터 주의
'''

a = input().strip()
b = input().strip()
la = len(a)
lb = len(b)

LCS = [[0]*(lb+1) for _ in range(la+1)]

for i in range(1,la+1):
    for j in range(1,lb+1):
        if a[i-1] == b[j-1]:        # 두 문자열 끝이 같은 문자란 뜻 (문자열에선 인덱스 0부터 세므로 -1씩해줌)
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])

print(LCS[-1][-1])

