'''
<input>
N M  # 수 개수, 합 구해야하는 횟수
N개의 수들
i, j #M개만큼의 i, j들
i, j

1. 테이블 정의
D[i] = 1번째부터 ~i번째 수 만큼 더했을 때의 합

2. 점화식
D[n] = D[n-1] + nums[n]

3. 초기값
D[1] = nums[1]

4. 답
ans = D[j] - D[i-1]
'''
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
nums = list(map(int, input().split()))
d = [0] * (len(nums) + 1)  # 1~n까지 쓸거임
# 테이블 값 설정 -> O(N)
for k, num in enumerate(nums):
    d[k + 1] = num + d[k]
# 답 출력
for _ in range(m):
    i,j = map(int, input().split())
    print(d[j]-d[i-1])