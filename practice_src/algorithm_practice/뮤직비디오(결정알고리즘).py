# 이분탐색

n, m = map(int, input().split())
playlist = list(map(int, input().split()))

def count_dvd(mid): # mid로 설정된 용량으로 분할시 몇개로 분할됨?
    summ = 0
    cnt = 1
    for x in playlist:
        if summ + x > mid:
            summ=x
            cnt += 1
        else:
            summ += x
    return cnt



# 1. 최대 용량부터 가능 하기 때문에 최대용량부터 시작해서 줄여나가야 함
largest = sum(playlist)
maxx = max(playlist)
lt = 1
rt = largest
res = 0
while lt<=rt:
    mid = (lt+rt)//2    # DVD 1장의 용량
    if mid >= maxx and count_dvd(mid) <= m: # 분할 된 dvd 개수가 m보다 작다면? 용량이 너무 크다는 거니까 줄여야 함
        res = mid   # 일단 답에 갱신해놓기
        rt = mid-1
    else:
        lt = mid+1 # 불가능하다면 용량 늘리기(mid로 설정한 용량이 마지막 남은 용량을 수용 못하는 것이니까)

print(res)

