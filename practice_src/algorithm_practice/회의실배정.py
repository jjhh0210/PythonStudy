#greedy
import sys
n = int(sys.stdin.readline())
times = []
for _ in range(n):
    s,e = map(int,sys.stdin.readline().split())
    times.append((s,e))

# 회의 끝나는 시간기준 오름차순 정렬
# 끝나는 순위를 먼저 고려하고, 끝나는 순위가 같다면 시작 시간순으로 정렬!
times.sort(key=lambda x : (x[1] ,x[0]))

# 현재 회의 끝나는 시간 <= 새롭게 시작할 회의 시작 시간 이여야 회의 가능
cnt = 0
end = 0
for s,e in times:
    if end <= s:
        end = e
        cnt+=1

print(cnt)



