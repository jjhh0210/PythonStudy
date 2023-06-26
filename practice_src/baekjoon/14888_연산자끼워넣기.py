# from itertools import permutations
# n = int(input())
# number = list(map(int, input().split()))
# op = list(map(int, input().split()));
# operator = '+' * op[0] + '-' * op[1] + '*' * op[2] + '/' * op[3]
# operator_perm = permutations(operator, n-1)
#
# max_result = - int(1e9)
# min_result = int(1e9)
# for perm in operator_perm:
#     result = number[0]
#     for i in range(1, n):
#         if perm[i-1] == '+':
#             result += number[i]
#         elif perm[i-1] == '-':
#             result -= number[i]
#         elif perm[i-1] == '*':
#             result *= number[i]
#         elif perm[i-1] == '/':
#             if result < 0 and number[i] > 0:
#                 result = -1*( result*(-1) // number[i])
#             else:
#                 result //= number[i]
#     max_result = max(max_result, result)
#     min_result = min(min_result, result)
#
# print(max_result)
# print(min_result)


# 순열 라이브러리 없이 DFS로 풀기 - 완전탐색
#가지치기 불가능함. 왜냐하면 끝까지 연산을 해봐야 최종 결과값을 알수있음.
n = int(input())
arr = list(map(int, input().split()))
add, sub, mult, div = map(int, input().split())

minn, maxx = float('inf'), float('-inf')

def dfs(L, summ):
    global n, add, sub, mult, div, minn, maxx
    if L == n:
        maxx = max(maxx,summ)
        minn = min(minn,summ)
    else:
        if  add>0:
            add-=1
            dfs(L+1,summ+arr[L]) #1번원소부터 더해나가기 시작!
            add+=1
        if sub>0:
            sub-=1
            dfs(L+1,summ-arr[L]) #1번원소부터 더해나가기 시작!
            sub+=1
        if mult>0:
            mult-=1
            dfs(L+1,summ*arr[L]) #1번원소부터 더해나가기 시작!
            mult+=1
        if div>0:
            div-=1
            if summ<0 and arr[L] > 0: # 음수를 양수로 나눌 경우 -> 양수로 바꾼 후 나눈 몫에 - 붙임
                dfs(L+1,-((-summ)//arr[L]))
            else:
                dfs(L+1,summ//arr[L])
            div+=1
dfs(1,arr[0])#인덱스
print(maxx)
print(minn)











