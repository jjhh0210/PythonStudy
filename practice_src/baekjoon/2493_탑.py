import sys
input = sys.stdin.readline

def solution(n, towers):

    ans = [0]*n
    stack = [1]     # 타워 idx 스택(idx:0을 1부터 취급)
    for i,tower, in enumerate(towers):
        if i==0:
            continue
        # 스택탑 갱신(나보다 높이 낮은애들 다 제거)
        while stack and tower > towers[stack[-1]-1]:
            stack.pop()

        # 여기까지 온다면 무조건 나는 stack top보다 높이 크거나 같음
        if not stack: # stack이 비었으면
            ans[i]=0
        else:        # 안비었으면
            ans[i]=stack[-1]
        stack.append(i+1)
    return ans

if __name__ == '__main__':
    n = int(input())
    towers = list(map(int, input().split()))
    ans = solution(n, towers)
    print(*ans)
