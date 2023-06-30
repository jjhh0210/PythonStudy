n = int(input())

## i + summ(i의 각자리수) == n이면 됨
# minn = float("inf")
for i in range(1,n):
    summ = sum((map(int, str(i))))  #각 자리수의 합을 구함
    if i+summ == n:
        print(i)
        break
else :
    print(0)



