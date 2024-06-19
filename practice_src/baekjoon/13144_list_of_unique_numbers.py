'''
- 길이가 N인 수열이 주어질 때, 수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러 번 등장하지 않는 경우의 수를 구하는 프로그램을 작성하여라.
<input>
5
1 2 3 4 5
-> 15
ㅡㅡㅡㅡㅡㅡㅡㅡㅡ
'''
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
##### 방법 1. 전체 경우의 수 - 중복되는 경우의 수
# # 전체 경우의 수
# ans = n*(n+1)//2
#
# # 중복 되는 경우 구하기
# l = 0
# ct = Counter()
# for r,num in enumerate(arr):
#     ct[num]+=1
#     while ct[num]>1:    # 중복 숫자 발생한 순간
#         ans-=n-r        # 1. n-r개를 뺌
#         ct[arr[l]]-=1   # 2. counter에서 빼고
#         l+=1            # 3. l 한 칸 이동

##### 방법 2. '중복 숫자 없는' l~r 까지 arr[r]을 포함한 부분 수열 개수를 더해감
# ex.[1,2,3,4] 이고 l=0,r=2이면 [3],[3,2],[3,2,1] 3개!!==r-l+1
visited = [False]*100001
ans,l = 0,0
for r in range(n):
    while l<r and visited[arr[r]]:
        # l이 중복된 수 다음까지 찾아가야 함
        visited[arr[l]]=False
        l+=1
    ans+=(r-l+1)
    visited[arr[r]]=True

print(ans)