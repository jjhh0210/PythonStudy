#1. 유클리드 호제법으로 최대공약수 구함
#2. 최소공배수 = A * B / 최대공약수

n = int(input())
for _ in range(n):
    x,y = map(int, input().split())
    a,b = max(x,y), min(x,y)

    while b:            #b!=0일동안
        a,b = b,a%b     #b가 0이 되면 a가 최대공약수임
    print(x*y//a)       #최소공배수
