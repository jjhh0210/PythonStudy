ans = 0
def dfs(S,summ,n,ts,ps):
    global ans
    if S == n:
        ans = max(ans, summ)
    else:
        next_s = S+ts[S]
        next_sum = summ+ps[S]
        if next_s <= n: # 주의) next_s == n 이라는 것은, n-1(휴가전날) 까지 상담하고, 그 다음 상담이 n부터 이므로 가능!!!!
            # 현재 상담 진행할 경우 (단, 다음 시작날짜가 n 전 일때만 가능)
            dfs(next_s,next_sum,n,ts,ps)
        # 현재 상담 진행 x 경우
        dfs(S+1,summ, n,ts,ps)

def solution(n,ts,ps):
    dfs(0,0,n,ts,ps)
    return ans
if __name__ == '__main__':
    n = int(input())
    ts = [0]*n
    ps = [0]*n
    for i in range(n):
        t,p = map(int, input().split())
        ts[i] = t
        ps[i] = p
    print(solution(n,ts,ps))
