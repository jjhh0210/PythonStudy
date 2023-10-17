# import sys
# import copy
# from collections import deque
#
#
# # 방향에 따라 모든 원소 이동 및 합치기
# def merge(board,dir):
#     global n
#     # 위
#
#     # 오른
#     # 아래
#     if dir == 3:
#         for j in range(n):
#             stack = deque()
#             # 한 줄마다 확인
#             for i in range(n-1,-1,-1):
#                 ## 1. 스택에 집어넣기
#                 if board[i][j] >0:
#                     temp = board[i][j]
#                     flag = False
#                     # 맨 위 원소와 비교해서 합칠 수 있는지 확인
#                     if len(stack)>0 and stack[-1][0] == temp and stack[-1][1]==False:
#                         # 합침
#                         stack.pop()
#                         temp = temp*2
#                         flag = True
#                     stack.append((temp,flag))
#                     board[i][j]=0
#
#             ## 2. 스택에서 빼서 이동 후 값으로 재할당
#             for idx, item in enumerate(stack):
#                 board[n-1-idx][j] = item
#
# def dfs(board, depth):
#     global ans
#     if depth ==5:
#         # 최대 블록 찾기
#
#
#         return
#
#     temp = copy.deepcopy(board)
#     for dir in range(4):
#
#
#
#
#
#
#
#
# ## main ##
# sys.stdin = open("input.txt", "r")
# T = int(input())
#
# for test_case in range(1, T + 1):
#     n = int(input())
#     ans = 2 # 최대 블록 구하기
#
#     # 보드 초기화
#     board = [[0]*n for _ in range(n)]
#
#     # 보드 입력
#     for i in range(n):
#         row = list(map(int, input().split()))
#         for j in range(n):
#             board[i][j] = row[j]
#
#     # 방향
#     # 0:왼, 1:위, 2:오른, 3:아래
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#
#     if n==1:
#         print(board[0])
#     else:
#         dfs(board, 0)
#         print(ans)
