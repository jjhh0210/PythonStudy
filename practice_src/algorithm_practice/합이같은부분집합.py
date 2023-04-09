n = int(input())
a = list(map(int,input().split()))
total = sum(a)

found = False
def dfs(v,summ):
    global found

    if found or summ > total//2:   # summ이 전체합의 반보다 커지거나 이미 yes경우 찾았을 시 더 탐색x,
        return
    if v == n:  # 얘는 인덱스 0부터 시작이라 v==n
        #종료조건
        if total-summ == summ:
            found = True
    else:
        dfs(v+1,summ+a[v])  #a[v] 선택 o
        dfs(v+1,summ)       #a[v] 선택 x
dfs(0,0)

print("YES" if found else "NO")





