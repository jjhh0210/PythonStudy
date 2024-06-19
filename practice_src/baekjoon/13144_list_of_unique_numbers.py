'''
- 길이가 N인 수열이 주어질 때, 수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러 번 등장하지 않는 경우의 수를 구하는 프로그램을 작성하여라.
<input>
5
1 2 3 4 5
-> 15
ㅡㅡㅡㅡㅡㅡㅡㅡㅡ
- 전체 경우의수 - 중복되는 경우의수 구하기
'''
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
# 전체 경우의 수
ans = n*(n+1)//2

# 중복 되는 경우 구하기
l = 0
ct = Counter()
for r,num in enumerate(arr):
    ct[num]+=1
    while ct[num]>1:    # 중복 숫자 발생한 순간
        ans-=n-r        # 1. n-r개를 뺌
        ct[arr[l]]-=1   # 2. counter에서 빼고
        l+=1            # 3. l 한 칸 이동
print(ans)