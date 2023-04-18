
# a = list(map(int, input().split()))
# summ = 0
# lt = 0
# flag = True
# for rt in range(1,len(a)):
#     flag = False
#     if a[rt] > a[lt]:
#         flag = True
#         while lt<rt:
#             summ+=a[rt]
#             lt+=1
#     else:
#         summ+=a[rt]
#         lt+=1
#
# print(summ)
from collections import deque
a = [15,14,13,12,11]
summ = 0
stack = deque()
seq = [0]*len(a)

for i in range(len(a)):
    while stack and (stack[-1][1] > a[i]):
        idx,tmp = stack.pop()
        seq[idx] = a[i]
    stack.append((i,a[i]))

# print(sum(seq)+sum(stack[1]))
print(seq)
print(stack)




import itertools
b= itertools.permutations(4,2)
print(b)
# 40 7 15 12
# 38 -> 7 7 12 12

# 5
# 1 15
# 2 14
# 3 13
# 4 12
# 5 11

#61