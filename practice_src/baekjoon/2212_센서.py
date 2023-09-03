import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
sensors = sorted(list(map(int, input().split()))) # 센서 정렬

####센서 간 간격 구하기####
# 집중국>=센서개수 경우(센서 1개일 때 포함) -> 센서 마다 하나씩 해서 수신가능길이 0
if k>=n:
    print(0)

# 센서가2개 이상일 경우 -> 전체 간격 중 가장 큰 거부터 K-1개 제거 후 모두 sum
else:
    max_gap = []
    for i in range(1,n):
        max_gap.append(sensors[i]-sensors[i-1])
    max_gap.sort(reverse=True)
    print(sum(max_gap[k-1:]))
