#Bottom up
n=int(input())
dy=[0]*(n+1)    # 돌 개수당 건널 수 있는 방법의 수

dy[1]=1
dy[2]=2
for i in range(3, n+2):
    dy[i]=dy[i-1]+dy[i-2]

print(dy[n+1])
