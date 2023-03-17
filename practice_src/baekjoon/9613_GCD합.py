import math
t = int(input())

def GCD(x,y):
    a,b = max(x,y),min(x,y)
    mod = a%b
    while mod>0:
        a,b = b,mod
        mod = a%b
    return b

for _ in range(t):
    case = list(map(int,input().split()))
    n = case[0]
    sum = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
           sum +=GCD(case[i],case[j])  #math.gcd()사용해도 시간 크게 차이 없긴함
    print(sum)



