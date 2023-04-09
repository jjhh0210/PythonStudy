# greedy
n = int(input())
p = list(map(int, input().split()))
summ = 0
p.sort()    #오름차순 정렬
m = len(p)
# my풀이 - 필기참고
# for x in p:
#     summ+=m*x
#     m-=1
# print(summ)

# 풀이2 - p[0:x] 까지의 합을 계속해서 더함
for x in range(1,n+1):
    summ += sum(p[0:x])
print(summ)



