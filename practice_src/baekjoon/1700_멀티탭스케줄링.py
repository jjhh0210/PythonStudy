'''
- 전기용품 사용 순서 -> 플러그 빼는 최소 횟수
<input>
2 7     # 멀티탭 구멍 개수 N, 전기 용품 총 사용 횟수 K
2 3 2 3 1 2 7   # 전기용품 사용 순서 및 종류(종류: K이하 자연수)
정답: 2
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
우선순위 :  가장 멀리 떨어져 있는 것 -> 가장 적은 것
'''
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

info = {}   # 전기용품 종류별 위치순서
for pos,item in enumerate(arr) :
    if info.get(item) == None:
        info[item] = deque([pos])
    else:
        info[item].append(pos)
ans = 0
tab = []
cnt = 0
for i in range(k):
    item = arr[i]
    info[item].popleft()     # 현재 사용 item은 무조건 info에서 빼주기
    if not info[item]: info[item] = [101]   # 비면 101로 초기화

    if item in tab:            # 코드 이미 꽂혀있는 경우 pass
        continue
    if cnt < n:                 # 코드 그냥 꽂을 수 있는 경우
        tab.append(item)
        cnt+=1
    else:            # 다른 것 뽑고 꽂아야 하는 경우
        # 뽑을 것 탐색 -> 우선순위: 가장 멀리 떨어져 있는 것 -> 가장 적은 것
        mx = tab[0]
        for c in tab:
            clen, cpos, mxlen, mxpos = len(info[c]), info[c][0], len(info[mx]), info[mx][0]
            if (-cpos, clen) < (-mxpos, mxlen): # 첫번째가 같으면 두번째 비교 (갱신 조건: 1번이 더 커야함. 1번이 같으면 2번이 더 작아야함 의미)
                mx = c
        tab.remove(mx)
        tab.append(item)
        ans+=1

print(ans)

'''
3 10
1 2 3 4 4 5 2 1 1 4
result : 3

3 5
1 1 1 1 1
result : 0

1 10
1 2 3 4 5 6 7 1 2 3
result : 9

2 9
1 2 3 1 2 3 1 2 3
정답: 4

3 13
2 3 4 2 3 4 1 5 5 5 2 3 2
정답: 2(4를 뽑고 1을 넣고, 1을뽑고 5를 넣으면 됨)

**주요 반례** -> 7나와서 우선순위 순서 바꾸니까 해결. (0 pos 가장 멀리 있는 것 -> 배열 길이 적은 것 으로 바꾸니까 됨)
2 15
3 2 1 2 1 2 1 2 1 3 3 3 3 3 3
정답: 2
'''
