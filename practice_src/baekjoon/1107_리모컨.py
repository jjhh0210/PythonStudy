target = int(input())

ans = abs(100 - target)     #초기값 -> +나 -로만 이동할 수 있는 경우
m = int(input())            #고장난 버튼 개수
if m:                       #0이 아니면
    broken = set(input().split())   #고장난 버튼 모음
else :
    broken = set()
# 완전 탐색으로 풀기
for num in range(1000001):
    for n in str(num):
        if n in broken: #수 중 고장난 숫자 있는경우
            break
    else:   #고장난 숫자 없어서 다 누른 경우 -> ans랑 (숫자길이+부족한만큼 +나-누른 개수) 중 작은거
        ans = min(ans, len(str(num))+abs(num-target))

print(ans)





