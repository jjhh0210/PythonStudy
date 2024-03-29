'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
'''
import sys
input = sys.stdin.readline

n = int(input())
d = [0]*1000001 #10의 6승까지의 인덱스 쓰려면!!
d[1] = 0    # 초기값설정

# d[i] : i를 1로 만들기 위해 필요한 연산 사용 회수 최소값
for i in range(2, n+1): # 2부터 n까지 for문을 돌며 d[i] 갱신
    d[i] = d[i-1]+1;    # -1은 무조건 수행하니까..
    if i%3==0:
        d[i] = min(d[i], d[i//3]+1)
    if i%2==0:
        d[i] = min(d[i],d[i//2]+1)
print(d[n])