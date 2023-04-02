n,k = map(int,input().split())
price = list(map(int, input().split()))

lt = 0
max_len = 0
max_rt = 0
max_lt = 0
cnt = 0

for rt in range(0,n):
    if price[rt-1] > price[rt] and rt!=0:
        cnt+=1 # 전날보다 주가 하락시 cnt
    while cnt>k: # cnt == k 될 때까지 lt 증가
        if price[lt] > price[lt+1]:
            cnt-=1
        lt+=1
    # 최대 연속된 구간 길이, 그 때의 lt와 rt 갱신
    if rt-lt+1 >= max_len: #정답이 여러개 라면, 마지막 날이 가장 늦는 것을 출력
        max_len = rt-lt+1
        max_rt = rt+1   # 인덱스는 0부터 시작인데 출력시에는 첫째날부터니까 +1해줘야
        max_lt = lt+1

print(max_lt, max_rt)

