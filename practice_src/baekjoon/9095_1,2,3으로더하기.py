'''
D[i] = i를 1, 2, 3의 합으로 나타내는 방법의 수라고 정의
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    d = [0] *12  # d=[0]*(n+1)라고 하면? 에러남!
    d[1],d[2],d[3] = 1,2,4  # n이 1 or 2인경우, d[3]이 없어서 초기화 시 인덱스 에러! 따라서 리스트 크기는 넉넉하게

    for i in range(4,n+1):
        d[i] = d[i-1]+d[i-2]+d[i-3]

    print(d[n])

