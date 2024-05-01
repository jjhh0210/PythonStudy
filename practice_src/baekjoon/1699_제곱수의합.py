'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14
1 2 3 1 2 3 4 2 1 2  3  4


'''


n = int(input())
d = [i for i in range(n+1)]
d[1] = 1

for i in range(2,n+1):
    num = i**(1/2)    #루트값
    if num.is_integer():
        d[i]=1
    else:
        z = int(num)
        while z>0:
            d[i] = min(d[i-z**2]+d[z**2],d[i])  # d[i-z*z]+1 (사실 d[z**2]=1임..)
            if d[i]==2: break   # 최소값인 2가 나오면 바로 break
            z-=1

print(d[n])
