'''
- N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
- 존재하면 1, 아니면 0 출력

<input>
5               # N (1~100000)
4 1 5 2 3       # N개의 정수 A배열
5               # M (1~100000)
1 3 7 9 5       # M개의 A안에 존재하는지 알아낼 수들
<output>
1
1
0   (7)
0   (9)
1
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
- 정수의 범위가 -2^31~2^31이므로 존재확인 배열 만들기 불가능 ( O(N) )
- 선형탐색시 -> O(NM)
- 정렬 후 이진 탐색시 -> O(NlogN+MlogN)
'''
def binarysearch(target):
    s = 0
    e = n-1
    while s<=e:
        mid = (s+e) // 2
        if a[mid]==target:
            return 1
        if a[mid]>target:
            e = mid-1
        else:
            s = mid+1
    return 0

import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
# 1. 정렬
a.sort()
# 2. 탐색
for num in nums:
    print(binarysearch(num))

