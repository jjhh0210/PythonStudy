n = int(input())
# for i in range(1,n):
#     if (2*i-3) < 0:
#         print(' '*(n-i) + '*')
#     else:
#         print(' '*(n-i) + '*' + ' '*(2*i-3)+'*')
# print('*' * (2 * n - 1))

## 다른방법 -> 첫번째 줄과 마지막줄을 한 코드로 합칠 수 있음
for i in range(1,n+1):
    if i==1 or i==n:
        print(' '*(n-i) + '*' * (2*i-1))
    else:
        print(' '*(n-i) + '*' + ' '*(2*i-3)+'*')
