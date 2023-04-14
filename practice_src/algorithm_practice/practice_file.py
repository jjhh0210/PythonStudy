import copy
a = [[-2,2,3],[1,2,9]]
# 2차원 배열의 최대, 최소 구하기!!!
s = min(map(min, a))
e = max(map(max, a))
print(s,e)
b = copy.deepcopy(a)
b[0].append(10)
print(a)
print(b)

mapp = list(map(int, input()))
print(mapp)
