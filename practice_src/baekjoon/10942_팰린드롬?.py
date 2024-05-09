'''
<input>
자연수 N개 적음, 질문 M번 (1<=S<=E<=N)
S번째 수~E번째 까지 수 팰린드롬을 이루는지를 물어봄

<output>
펠린드롬 1, 아니면 0

1.DP사용가능한지
겹치는 부분문제(부분문제가 반복되어 재사용 가능) O, 최적 부분 구조 O

2. 테이블 정의
d[s][e] = s~e번째까지 팰린드롬인지 아닌지

3. 점화식
1) s,e에 있는 수가 다르면 팰린드롬이 아님
2) s,e에 있는 수가 같다면
    2-1) 길이가 1 (s바로다음 e)이면 무조건 팰린드롬
    2-1) 길이가 1이상: s+1, e-1에 있는 수가 팰린드롬이어야 팰린드롬임 (즉, d[s][e]는 d[s+1][e-1]여부와 같다)

if arr[s] != arr[e] : d[s][e] = 0
else:
    d[s][e] = d[s+1][e-1]

<EX>
    1 2 1 3 1 2 1
- 2~5가 팰린드롬일려면? -> 3~4 (s+1, e-1)가 팰린드롬이어야!!
- 우측 하단 대각선 방향으로 차례대로 채운다
- == 길이 0~N-1 순서( 1,1 2,2 ... -> 1,2 2,3 ... -> 1,3 2,4 ...-> 1,4 2,5 ...)
    0 1 2 3 4 5 6 (e)
0   1 0 1 0 0 0 1
1     1 0 0 0 1 0
2       1 0 1 0 0
3         1 0 0 0
4           1 0 1
5             1 0
6               1
(s)

'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

d = [[0]*n for _ in range(n)]

# 초기화(1,1/ 2,2 /3,3 다 팰린드롬==1)
for i in range(n):
    d[i][i]=1

# 테이블 채우기
for l in range(1,n):  # l = s-e (s,e 길이 차이)
    for s in range(n-1):    # 마지막 바로 전의 원소까지 start
        if s+l >= n : continue   # e의 범위가 넘어가면 pass
        e = s+l
        if arr[s] != arr[e]:
            d[s][e] = 0             # 수가 다르면 팰린드롬 아님
        else:
            d[s][e] = d[s+1][e-1] if l>1 else 1


for _ in range(m):
    s,e = map(int, input().split())
    print(d[s-1][e-1])

