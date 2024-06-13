'''
- a[i] + a[j] + a[k] = a[l] 을 만족하는 a[l] 중 최댓값을 구하라.
- ⭐️2개의 값을 묶은 후 어느 한쪽의 값을 이분탐색으로 찾아서 시간복잡도를 낮추는 아이디어는 이분탐색 관련 응용문제에서 핵심적으로 많이 나오는거

2 3 5 10 18
i j  k  l
3+5+10=18   # 가장 큰 수
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
O(N^4) : i,j,k,l에 대한 4중 포문
O(N^3lgN): i,j,k 3중 포문, i+j+k 값이 배열 a에 있는지 이분탐색

두 원소의 합 배열 two만들기(길이&시복:N^2) -> two[m]+a[k] = a[l]을 만족하는 a[l]중 최댓값
two[m] = a[l]-a[k]
O(N^2lgN):k,l에 대한 이중포문,a[l]-a[k]가 배열 two 안에 잇는지 확인하기.
    O(N2lg(N2)) = O(N2 * 2lgN) = O(N2lgN)

'''
import sys
input = sys.stdin.readline

n = int(input())
a = [0]*n
for i in range(n):
    a[i] = int(input())

two = []
for s in range(n):
    for e in range(s,n):
        two.append(a[s]+a[e])
two.sort()
# i,j 고른 후 two에 a[i]-a[j] 있는지 이분탐색
# 해시로 함 -> n + n2 / 이분탐색은 n2*lgn 아님?
maxx = 0
for i in range(n):
    for j in range(n):
        # 이분탐색
        target = a[i]-a[j]
        if target<0: continue   # 음수이면 넘어가기
        s = 0
        e = len(two)-1
        while(s<=e):
            mid = (s+e)//2
            if two[mid]==target:
                maxx = max(a[i], maxx)
                break
            elif two[mid]< target:
                s = mid+1
            else:
                e = mid-1
print(maxx)
