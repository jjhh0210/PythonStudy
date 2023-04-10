n,m = map(int, input().split())
cnt = 0 #경우의 수 세기
ch = [0] * (n+1) # 체크 배열 :1~n까지 수
p = [0]*m    # 순열
def dfs(L):
    global cnt, ch, p
    if L==m:
        cnt+=1
        print(*p)
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i] = 1   # 뽑은 숫자 check
                p[L]=i  #헷갈리지 말기~
                dfs(L+1)
                ch[i] = 0   # 백트랙 되면 뽑았던 숫자 uncheck
dfs(0)
print(cnt)