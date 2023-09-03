import sys, heapq

n = int(sys.stdin.readline())
lst = [0]*n
for i in range(n):
    s,e = map(int, sys.stdin.readline().split())
    lst[i] = (s,e)

#lst.sort(key = lambda x: (x[1], x[0])) #끝나는 시간 기준으로 오름차순 정렬
lst.sort() # 강의 시작 시간 기준 오름차순 정렬


hq = [] # 회의실 별 끝나는 시각 우선 순위 큐
for s,e in lst:
    if hq and hq[0] <= s : #  첫번째 원소가 아니며, 가장 빨리 끝나는 회의 이후 시작할 수 있는 회의이면 pop후 push
        heapq.heappop(hq)
    heapq.heappush(hq,e)    # pop안하고 push -> 무조건 새로운 회의실 생성!
    print(hq)

print(len(hq))

