n = int(input())
a = list(map(int,input().split()))

original = []
for num in range(n,0,-1):
    idx = a[num-1]
    original.insert(idx,num) #큰 수 부터 돌면,역수열의 값이 곧 들어갈 인덱스임
    # print(num, a[num-1], original)

print(*original)

# n=int(input())
# a=list(map(int, input().split()))
# seq=[0]*n
# for i in range(n):
#     for j in range(n):
#         if(a[i]==0 and seq[j]==0):
#             seq[j]=i+1
#             break
#         elif seq[j]==0:
#             a[i]-=1
#
# for x in seq:
#     print(x, end=' ')