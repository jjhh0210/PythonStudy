import sys
n,k = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

# 각 i, i+1 의 차이 배열 구하기
# why? 차이가 가장 큰 애들 사이부터 차례대로 분할해야함
arr_gap = [ arr[i]-arr[i-1] for i in range(1,n)]

# 차이 배열 역순 정렬
arr_gap.sort(reverse=True)

# k개의 조를 만듦 -> 차이 가장 큰거부터 K-1개 없애면 최소합임!
print(sum(arr_gap[k-1:]))