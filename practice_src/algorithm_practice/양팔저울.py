def dfs(L,summ, k, G,possible):
    global ans
    if L == k:
        if 0<summ<= sum(G):
            possible.add(summ)
    else:
        dfs(L+1,summ+G[L],k,G,possible) # 왼쪽에 추를 놓음
        dfs(L+1,summ-G[L],k,G,possible) # 오른쪽에 추를 놓음
        dfs(L+1,summ,k,G,possible)          # 추를 놓지 않음

def solution(k,G):
    ans = 0
    possible = set()
    dfs(0,0,k,G,possible)
    ans = sum(G)-len(possible)
    return ans


if __name__ == '__main__':
    k = int(input())
    G = list(map(int, input().split()))
    print(solution(k,G))