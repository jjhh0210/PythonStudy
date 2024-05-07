'''
4 6
010010
011111
101101
011111
'''

n,m = map(int, input().split())
mapp = [ list(map(int, input())) for _ in range(n)]

# 단일 행/열일 때 like (1,5) or (5,1) 주의
ans = 0
for i in range(n):
    for j in range(m):
       if mapp[i][j] ==1:
           if i >=1 and j >= 1:
               mn = min((mapp[i-1][j-1], mapp[i-1][j], mapp[i][j-1]))
               mapp[i][j] = mn+1
           ans = max(ans, mapp[i][j])

print(ans**2)
# for a in mapp:
#     print(a)