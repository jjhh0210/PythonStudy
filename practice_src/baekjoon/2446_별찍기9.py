n = int(input())

# for i in range(2*n-1):
#     if i < n :
#         print(' '*i + '*'*(2*(n-i)-1))
#     else:
#         print(' ' * (2*n-i-2) + '*' * (2*(i-n)+3))

# for문 2개로 찍기
for i in range(n):
    print(' ' * i + '*' * (2 * (n - i) - 1))
for i in range(n-2,-1,-1): #n-2부터 0까지 -1하며 반복
    print(' ' * i + '*' * (2 * (n - i) - 1))