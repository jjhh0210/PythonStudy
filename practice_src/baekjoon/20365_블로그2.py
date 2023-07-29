import sys

n = int(sys.stdin.readline())
brlist = list((sys.stdin.readline()).strip())   # readline은 입력값의 개행문자도 받기 때문에 strip

start_ch = brlist[0]    
ans = 1
prev_ch = start_ch
# 처음 문자와 반대의 문자 들만 세면 됨
for ch in brlist:
    if ch != start_ch and prev_ch==start_ch: # 연속 되지 않은 반대 문자일 경우 +1
        ans+=1
    prev_ch = ch # 갱신
print(ans)
