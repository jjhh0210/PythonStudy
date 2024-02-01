'''
1. 한칸 or 두칸
2. 연속 세칸 X, 한칸은 연속 두 번만 가능
마지막에 도달했을 때, 총 점수의 최댓값 구하기
'''
import sys
input = sys.stdin.readline

n = int(input())
answer = 0
scores = [0]*(n+1)
for i in range(1,n+1):
    scores[i] = int(input())
'''1. D[i] = [i번째 계단까지 올라섰을 때 점수 합의 최댓값, i-2에서 i번째로 건너뛰어 왔을 때 점수합의 최댓값]'''
## 0 : 시작, 1~n : 계단
D = [[0,0] for _ in range(n+1)]   # 최소 1개의 계단
D[1] = [scores[1],scores[1]] # [real max, max from -2]
if n<2:
    answer = scores[1]
else:
    # n>=2일경우
    for i in range(2,n+1):
        # real max 설정
        D[i][0] = max(D[i-2][0],D[i-1][1])+scores[i]  # max(2단계 전의 real max, 1단계 전의 max from -2)
        # max from -2 설정
        D[i][1] = D[i-2][0]+scores[i] # 다음 계단의 입장에서 1단계 전의 max from -2 == 현재의 max from -2 + 현재점수
    answer = D[n][0]
print(answer)

'''2. D[i] = i번째 계단을 안밟는다 쳤을 때, 밟지 않을 계단들 합의 최솟값, 
i번째 계단은 반드시 밟지 않을 계단!!'''
### 밟은 점수의 합 최대로 == 안밟은 점수의 합 최소로
## 즉, 최소로 선택하고, 점수 작은애들 우선으로 선택해야
## D[4] -> 1,2,3(무조건O),4(무조건X) -> 1,2중 안밟을 애 선택 (점수작은거)
## D[5] -> 1,2,3,4(O),5(X) -> 2,3중에 안밟을 애 선택

# D = [0]*(n+1)
# D[1],D[2],D[3] = scores[1],scores[2], scores[3]
# for i in range(4,n+1):
#     D[i] = min(D[i-2],D[i-3])+scores[i]
# print(sum(scores)-D[n])