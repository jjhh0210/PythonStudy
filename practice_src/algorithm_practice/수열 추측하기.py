from itertools import permutations
n,f = map(int, input().split())
b = [1]*n   #이항계수
cnt = 0
for i in range(1,n):        # 이항 계수 구하기 nC0 ~ nCn
    b[i] = b[i-1]*(n-i)//i
a = list(range(1,n+1))
# permutations(a) -> a의 순열들
for tmp in permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        sum+=x*b[L]
    if sum == f:
        print(*tmp)
        break
