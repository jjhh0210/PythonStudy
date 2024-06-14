'''
5           # 갖고 있는 숫자 카드 개수N
6 3 2 10 -10
8           # 찾아볼 개수 M
10 9 -5 2 3 4 5 -10 # 이 수들이 숫자카드에 몇개 있는가?

-> 있으면 1, 없으면 0
'''

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
ans = [0]*m

## 1. 이분탐색으로 풀기
cards.sort()# 이분탐색시 반드시 정렬!!!
for i, num in enumerate(nums):
    s,e = 0, len(cards)-1
    while s<=e:
        mid = (s+e)//2
        if cards[mid]==num:
            ans[i]=1
            break
        elif cards[mid]<num:
            s = mid+1
        else:
            e = mid-1

# ### 2. 딕셔너리로 풀기
# dic = {}
# for card in cards:
#     dic[card]=1
# for i, num in enumerate(nums):
#     if num in dic:
#         ans[i]=1
print(*ans)
