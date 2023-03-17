#유클리드 호제법으로 최대 공약수를 구해줌
#a,b의 최대공약수 -> 수만큼 1출력하면 됨
A, B = map(int, input().split())
def gcd(x,y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y

print('1' * gcd(A, B))