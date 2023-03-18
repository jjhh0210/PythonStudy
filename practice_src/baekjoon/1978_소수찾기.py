n = int(input())
nums = list(map(int,input().split()))

ans = 0
for num in nums:
    if num >1:
        ans+=1
        for i in range(2,int(num**(1/2))+1): #숫자의 제곱근까지만 확인
            if num%i == 0:
                ans-=1
                # print("not 소수:",num)
                break
print(ans)
