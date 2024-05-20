'''
- 그은 선의 총 길이 구하기
<input>
4       # N개 선을 그은 횟수
1 3     # s e ( - ~ +)
2 5
3 5
6 7
<output>
5
---------------------------------------
- s 순으로 정렬
- if 이전 e <  s : 선 끊김!!
  elif 이전 e >= s and 이전 e < e: 선 연장
  else: 선 중복이므로 pass
- 틀렸던 반례
3
1 6
2 3
4 5
-> 정답:5인데 6으로 나옴. 선이 아예 중복인 경우(else) 갱신하지 않는 조건 더해서 해결
'''
import sys
input = sys.stdin.readline

n = int(input())
pos = [ tuple(map(int, input().split()))for _ in range(n)]

pos.sort()
ps,pe = pos[0]
ans = pe-ps
for s,e in pos:
    if pe < s:  # 선 끊김
        ans+=e-s
    elif pe >= s and pe < e:    # 선 이어짐
        ans+=e-pe
    else:   # 선이 아예 중복인 경우엔 갱신 x!!! 불필요한 선이므로!!
        continue
    ps,pe = s,e

print(ans)
