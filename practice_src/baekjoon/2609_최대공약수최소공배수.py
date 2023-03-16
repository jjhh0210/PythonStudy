a,b = map(int,input().split())
minimum = min(a,b)
maximum = max(a,b)
#최대공약수
# for i in range(minimum,0,-1):   #min~2까지
#     if a%i == 0 and b%i == 0:
#         print(i)
#         break
#최대 공배수 -> 큰수의 배수가 작은수로 처음으로 나눠지면 최소공배수임
for i in range(1,minimum+1):
    if (maximum * i) % minimum == 0:
        print(maximum*i)
        break
