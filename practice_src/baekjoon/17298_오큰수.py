import sys
input = sys.stdin.readline

def solution(n,arr):
    ans = [0]*n
    ans[n-1]=-1
    stack =[arr[n-1]]

    # 탑이랑 거의 똑같은 문제!! 방향만 바뀜
    # 이중 for문 돌면 시간초과
    for i in range(n-2,-1,-1):
        now = arr[i]

        # 나보다 작거나 같은 애들 다 빼, 첨으로 큰애 찾음
        while stack and now >= stack[-1]:
            stack.pop()

        # 나보다 큰 애들
        if not stack:   # 스택 다 비움 -> 그럼 내가 지금 젤 크다는 뜻
            ans[i] = -1
        else:           # if stack!! 원소 1개 이상일 경우 -> top에 있는애가 오큰수
            ans[i] = stack[-1]
        stack.append(now)

    return ans

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))

    if n==1:    # 없어도 되긴함
        print(-1)
    else:
        ans = solution(n,arr)
        print(*ans)
