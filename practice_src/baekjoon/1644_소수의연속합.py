'''
- 한 자연수가 연속된 소수의 합으로 나타낼 수 있는 경우의 수
'''
import sys,math
input = sys.stdin.readline

n=int(input())
if n==1:
    print(0)
else:
    ## 소수 배열 만들기
    primes = [True]*(n+1)
    primes[:2]=[False,False]
    arr=[]  # 연속 된 소수 배열
    for i in range(2,int(math.sqrt(len(primes)))+1):
        if i:   # 소수의 배수
            for j in range(i*2,len(primes),i):
                primes[j]=False
    for i in range(len(primes)):
        if primes[i]:
            arr.append(i)
    # print(arr)
    ## 연속된 소수의 합의 경우의 수
    l = 0
    summ=0
    ans = 0
    for r in range(len(arr)):
        summ+=arr[r]
        while l<=r and summ>=n:
            if summ==n:
                ans+=1
            summ-=arr[l]
            l+=1

    print(ans)