import sys
input = sys.stdin.readline
'''
d[i] = i번째항으로 끝나는 연속 합 중 최대
-> i-1까지의 최대합 버림(0보다 작아서) VS i-1까지 최대합 살림  + i번째항 더하기
'''

n = int(input())
nums = list(map(int, input().split()))

d = [0]*n
d[0] = nums[0]  # 첫번재까지의 합
for i in range(1, n):
    # 0~i번째까지의 합
    d[i] = max(0,d[i-1])+nums[i]    # 이전까지의 부분합 + 현재 더할지 vs 아예 현재부터 시작할지

print(max(d))
