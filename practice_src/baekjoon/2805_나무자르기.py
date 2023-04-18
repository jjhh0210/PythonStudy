n,m = map(int,input().split())
trees = list(map(int, input().split()))

largest = max(trees)
lt = 1
rt =largest
summ = 0
while lt<=rt:
    summ=0
    mid = (lt+rt)//2

    # 구하기
    for tree in trees:
        if tree > mid:
            summ += tree - mid

    if summ < m :
        rt = mid-1
    else:
        res = mid
        lt = mid+1
print(res)
