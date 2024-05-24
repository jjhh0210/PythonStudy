'''
- 해당 수가 숫자카드 배열에 몇개 있는지 탐색
<input>
10      # 숫자카드 개수 N(1~500000)
6 3 2 10 10 10 -10 -10 7 3  # 숫자카드들
8           # M (1~500000)
10 9 -5 2 3 4 5 -10 # 몇개 가지고 있는지 확인해야할 정수들
정답: 3 0 0 1 2 0 0 2
'''
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

## 1. 딕셔너리로 풀이
# count = Counter(a)
# for num in nums:
#     if num in count:
#         print(count[num], end=' ')
#     else:
#         print(0, end = ' ')

## 2. 이분탐색 풀이 : 시작 위치, 끝 위치를 이분탐색으로 구함
def lower_idx(target, length):
    s = 0
    e = length
    while s<e:
        mid = (s+e)//2
        if a[mid] >= target:
            e = mid
        else:
            s = mid+1

    return s

def upper_idx(target, length):
    s = 0
    e = length
    while s<e:
        mid = (s+e)//2
        if a[mid]>target:
            e = mid
        else:
            s = mid+1
    return s

a.sort()
for num in nums:
    print(upper_idx(num,n)-lower_idx(num,n),end=" ")