# n = int(input())
# summ = 0
# cnt = 0
# lt = 1
#
# for rt in range(1 ,n):
#     summ += rt
#     if summ == n:
#         cnt+=1
#     while summ >= n:
#         summ -= lt
#         if summ == n:
#             cnt+=1
#         lt+=1
#
# print(cnt+1) # +1은 자기자신!


####### 절반까지만 돌면 훨씬 효율적이다! ######
n = int(input())
summ = 0
cnt = 0
lt = 1

if n == 1 or n == 2:
    print(1)
else:
    for rt in range(1, (n // 2) + 2): #3부터는 반만 돌아도 됨!!! 짝수인 경우 m = n//2 인데, 홀수인 경우를 위해 m = n//2 +1 까지 돌아야 함.
        summ += rt  # 더한다
        if summ == n:   # 변화가 생기면 확인한다
            cnt += 1
        while summ >= n:    # sum>=n이 되었으면 sum < n 이 될때까지 lt가 쫓아간다.
            summ -= lt
            if summ == n:   #변화가 생기면 확인한다.
                cnt += 1
            lt += 1
    print(cnt+1)

