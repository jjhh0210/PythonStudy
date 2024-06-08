'''
- 쉽게 말해 나보다 작은 수가 몇 개 있는지로 해석

<input>
5
2 4 -10 4 -9
-> 답: 2 3 0 3 1
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

2 4 -10 4 -9
2보다 작은 수: 2개
4보다 작은 수: 3개
-10보다 작은 수: 0개
-9보다 작은 수: 1개
'''

import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
narr = sorted(set(arr))  # -10 -9 2 4 (정렬 및 중복 제거)

## 방법1) 그냥 딕셔너리 활용하기
# dic = {}
# for i,item in enumerate(narr):
#     dic[item] = i
# for i,item in enumerate(arr):
#     arr[i] = dic[item]

## 방법2) 이분탐색으로 찾기!!
for i, target in enumerate(arr):
    s,e = 0,len(narr)-1
    while s<=e:
        mid = (s + e) // 2
        if narr[mid]> target:
            e = mid-1
        elif narr[mid]< target:
            s = mid+1
        else:
            arr[i] = mid
            break

print(*arr)
