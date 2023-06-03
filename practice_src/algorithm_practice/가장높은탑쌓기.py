n=int(input())
bricks=[]
for i in range(n):
    a, b, c=map(int, input().split())
    bricks.append((a, b, c))
bricks.sort(reverse=True)   #맨 앞에 잇는 밑면의 넓이에 대해 역순으로 정렬

dh = [0]*n # 현재까지의 최대 높이 저장
dh[0] = bricks[0][1]
res = 0     #최대 탑 높이
for i in range(1,n):
    max_h = 0
    for j in range(i,-1,-1):
        if bricks[i][2] <= bricks[j][2] and dh[j] > max_h:# 나보다 무게 무거운 것들 중 최대 탑 높이 높은애들 고르기
            max_h = dh[j]
    dh[i] = max_h + bricks[i][1]
    res = max(res,dh[i])

print(res)