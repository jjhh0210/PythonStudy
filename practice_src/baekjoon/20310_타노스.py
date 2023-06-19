s = list(input())
count_0, count_1 = s.count('0')//2, s.count('1')//2
# 배열의 순서를 유지하면서 사전순으로 가장 앞의 문자열을 찾아야함!!
chk = [True for _ in range(len(s))]
ans = ""
# 1. 앞에서 부터 1을 제거, 뒤에서부터 0을 제거
for i in range(len(s)):
    if count_1 ==0 :
        break
    if s[i] == '1':
        chk[i] = False
        count_1 -=1
for i in range(len(s)-1,-1,-1):
    if count_0 ==0 :
        break
    if s[i] == '0':
        chk[i] = False
        count_0 -=1

#2. true인 애들 합치기
for i in range(len(s)):
    if chk[i]:  # true이면
        ans+=s[i]
print(ans)