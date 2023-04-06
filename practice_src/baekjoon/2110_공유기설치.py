import sys
n,c = map(int, sys.stdin.readline().split())     # n개 집에 c개의 공유기를 배치 하려고 한다.
pos = []
for _ in range(n):
    pos.append(int(sys.stdin.readline()))
pos.sort()

def count_device(dist):
    # 가장 인접한 공유기 사이 거리가 dist일 때 배치 가능한 공유기 수 count
    # = 모든 공유기 사이 거리는 dist 이상이어야!
    cnt = 1 #맨 처음 집은 무조건 설치
    recent_installed = pos[0]
    for i in range(1,len(pos)):
        #  마지막으로 설치한 집과의 거리가 dist보다 작거나 같으면 공유기 배치 가능
        a = pos[i] - recent_installed
        # print(pos[i],"일 때 recent_installed과의 거리는 ",a)
        if a >= dist:
            cnt += 1
            recent_installed = pos[i]   # 가장 마지막으로 설치된 곳
            # print("거리",a,"니까 installed : ", recent_installed)
    return cnt

# 가장 인접한 공유기 사이 최대거리 -> 이분탐색 대상!
largest = max(pos)
lt = 1
rt = largest
res = 0

while lt <= rt:
    mid = (lt+rt)//2
    # print("**mid: ",mid)
    cnt_possible_device = count_device(mid)
    # print("배치 가능 공유기 수: ",cnt_possible_device)
    if  cnt_possible_device < c:
        # 가능한 공유기 배치 수가 c보다 작으면 -> 설정한 공유기 간 거리 너무 멈 -> 거리 줄여봐
        rt = mid-1
    else:
        # 가능한 공유기 배치 수가 c보다 크면 -> 설정한 공유기 간 거리 좁음 -> 거리 늘려봐
        # 최대 거리를 구하는 거니까 c랑 같아도 거리 더 늘려봐
        res = mid
        lt = mid +1

print(res)


