# 4,6,9,11 -> 30일까지
# 2월 -> 28일
# 나머지 31일까지
import sys
input = sys.stdin.readline

def solution(n,date):
    ans = 0
    arr =[0]*n
    # 날짜 파싱 ex) 12월1일 -> 1201, 5월31일 -> 531
    for i,d in enumerate(date):
        sm,sd, em,ed = d[0],d[1],d[2],d[3]
        arr[i] = (sm*100+sd, em*100+ed)

    # 피고 지는 날짜 오름차순 정렬
    arr.sort(key=lambda x: (x[0],x[1]))

    # 현재 선택된 꽃의 지는 날 (첨에는 301) -> 다음 꽃의 피는 날이 얘보단 작거나 같아야!
    target = 301
    start=0
    while target < 1201 and start < n:  # 꽃 선택
        # 일단 max 지는 날 target으로 초기화(가장 최소 값임)
        max_end = target

        # 다음으로 선택할 꽃
        for i in range(start,n):
            next_se = arr[i]    # 다음 꽃의 피고 지는 날
            # 피는 날이 target 이전, 지는 날은 target 이후
            if next_se[0]<= target: #  가장 지는 날이 늦은 꽃 찾기
                max_end = max(max_end,next_se[1])
            else:  # 피는 날이 target 보다 이후가 되면 stop
                start = i   # start 갱신
                break
        if max_end == target :  # 꽃 못찾은 경우(target보다 늦게 피는 애들만 있음)
            return 0    # 조건 만족 하는 꽃 선택 불가

        # max_end를 타겟으로 바꿈
        target = max_end
        
        #꽃 count
        ans+=1

    return ans


if __name__ == '__main__':
    n = int(input())
    date = [list(map(int,input().split())) for _ in range(n)]

    print(solution(n,date))