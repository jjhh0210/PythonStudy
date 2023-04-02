import sys
A = int(sys.stdin.readline())
prime = [True]*(A+1)
arr = []
for i in range(2,int(A**0.5)+1):
    #1. A까지의 나눠떨어지는 소수 찾기
    if prime[i]:
        j = 2
        while i*j<=A:
            prime[i*j] = False
            j+=1
        if A%i ==0:
            arr.append(i)

#2. 소수로 나눠떨어지고 나눠떨어지는 몫의 prime이 True이면 출력
for i in arr:
    if prime[A//i]:
        print(i,A//i)
        break
else:
    print("IMPOSSIBLE")




