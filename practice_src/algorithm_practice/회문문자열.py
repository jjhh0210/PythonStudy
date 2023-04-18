import re
s = input()
#1. 전처리
s = s.lower()
print(s)
s = re.sub('[^\w]','',s) #숫자,문자빼고 다 제거
print(s)
#2. 확인
if s == s[::-1]: #문자열 reverse
    print("YES")
else:
    print("NO")

##### deque 이용 ######
# from collections import deque
# dq = deque()
# ans = "YES"
# #1. al, num만 넣기
# for ch in s:
#     if ch.isalnum():
#         dq.append(ch.lower())
# while len(dq)>1:
#     if dq.popleft() != dq.pop():
#         ans = "NO"
#         break
# print(ans)
