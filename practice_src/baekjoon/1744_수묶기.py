# n = int(input())
# seq = []
# for _ in range(n):
#     seq.append(int(input()))
#
# #1. sort
# seq.sort()
#
# #2. 양수 음수 나누기
# pos = []
# neg = []
# i=0
# if len(seq)==1:
#     print(seq[0])
# else:
#     for i in range(len(seq)):       # 원소 1개일때 range(0,0)돼서 반복문이 안돌아가므로 따로 빼줘야 함
#         if seq[i] > 0:
#             neg.extend(seq[0:i])    # 0 ~ i까지 음수들(0포함)
#             pos.extend(seq[i:])   # i ~ 끝까지 양수들 -> 내림차순정렬
#             break
#     pos.sort(reverse=True)  #양수는 내림차순으로 정렬 후 큰수부터 묶어줘야함
#     # 음수일때
#     sum_neg = 0
#     sum_pos = 0
#     for i in range(0,len(neg),2):
#         if i+1 >= len(neg): # 개수가 홀수일 때 마지막 한개 남은 것은 그냥 더해줌
#             sum_neg += neg[i]
#         else:
#             sum_neg += neg[i]*neg[i+1]  #두개 곱해서 더하기
#     # 양수일 떄
#     for i in range(0,len(pos),2):
#         #
#         if i+1 >= len(pos): # 개수가 홀수일 때 마지막 한개 남은 것은 그냥 더해줌
#             sum_pos += pos[i]
#         elif pos[i+1] == 1: # i+1 수가 1일경우
#             sum_pos += pos[i]+pos[i+1]  #각각 더하기
#         else:
#             sum_pos += pos[i]*pos[i+1]  #두개 곱해서 더하기
#
#     print(sum_pos+sum_neg)
'''
두번째 시도
-1 2 1 3 -> 2*3 + -1 + 1
-1 1 2 3
0 1 2 4 3 5 -> 0+1+ 2*3 + 4*5
-1 0 1 -> -1*0 + 1
1 1 -> 1+1

->                  <-
-4 -3 -1 -1 0 // 1 1 3 4 5
-4 -3 -1 -1 0 5 4 3 1 1
1) 음수, 0
음수끼리 곱함 > 0이랑 곱함 -> 0 남으면 걍 pass
3) 1
무조건 더하기
4) 2~양수
끝에서부터 곱하기

'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = []    # 음의정수(0포함)

pos = []    # 자연수
ans = 0     # 최대 합
for _ in range(n):
    a = int(input())
    pos.append(a) if a>0 else arr.append(a)

arr.sort()
pos.sort(reverse=True)
arr.extend(pos) # -1 0 / 2 4 5 -> -4 4 3 3 1 1

if len(arr)==1:
    print(arr[0])
else:   # 수열 개수가 2이상
    q = deque(arr)

    ans = 0
    while q:    # n-2까지!!
        '''
        계산 경우 3가지: 나만 더하는 경우, 뒤에랑 더하는 경우, 뒤에랑 곱하는 경우
        # if q에 더이상 없음 -> 그거 더함
        # if 음수
        # elif 0,1
        # else 자연수(2이상)
        '''

        a = q.popleft()
        if len(q)==0:
            ans+=a
            break
        if a<0:
            # 뒤에가 자연수일 경우: 나만 더함
            # 뒤에가 0이하 음수일 경우: 무조건 곱함
            ans+= a if q[0]>0 else a*q.popleft()
        elif 0<=a<=1:
            ans+=a
        else:
            # 뒤에가 2이상일 경우: 무조건 곱함. 아니면(1) 무조건 더함
            ans += a*q.popleft() if q[0]>=2 else a+q.popleft()
    print(ans)