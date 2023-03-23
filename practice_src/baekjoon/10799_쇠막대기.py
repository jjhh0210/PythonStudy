from collections import deque
ps = input()

stk = deque()
sum = 0
for i,p in enumerate(ps):
    if p == "(":
        stk.append("(")
    else:
        stk.pop()
        if ps[i-1] == p: # 이전이 )인 경우 그냥+1
            sum += 1
        else:           # 이전이 (인경우 레이저이므로 남은 쇠막대기만큼 더함
             sum += len(stk)

print(sum)


