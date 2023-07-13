n = int(input())
drinks = list(map(int, input().split()))

drinks.sort(reverse=True)
# print(drinks)
a = drinks[0] # 가장 max = max + min/2 계속 반복
# for i in range(1,n):    # 1개 남을때까지
#     a += drinks[i]/2
print(a + sum(drinks[1:])/2)    # 그냥 가장 큰것 + 나머지 다 절반