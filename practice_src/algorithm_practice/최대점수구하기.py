# 최대 점수 구하기 -> 부분집합 구하기문제
# 바둑이 승차문제랑 비슷.. 그냥 선택 했다 안했다 백트래킹 하면서 각 조합의 합을 탐색하면 됨


def dfs(L, score_sum,time_sum,lst):
    global ans
    if time_sum > m :
        return
    if L == n:
        ans = max(ans, score_sum)
    else:
        dfs(L+1, score_sum+lst[L][0], time_sum+lst[L][1],lst) # L 선택 p
        dfs(L+1, score_sum, time_sum,lst)   # L 선택 x



def solution(n,m,lst):
    global ans
    lst = lst
    n = n
    m = m
    ans = float("-inf")

    dfs(0,0,0,lst)
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())  # 문제개수, 제한시간
    lst = []
    for _ in range(n):
        ps, pt = map(int, input().split())
        lst.append((ps, pt))
    print(solution(n,m,lst))


