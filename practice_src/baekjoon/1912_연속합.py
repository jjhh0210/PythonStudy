n = int(input())
a = list(map(int, input().split()))
max_ending_here = a[0] #이전까지의 부분합+현재 더할지 vs 아예 현재부터 시작할지 
maxx = a[0]    # 정답(전체에서 연속 최대 부분합)
for i in range(1,len(a)):
    max_ending_here = max(a[i],max_ending_here+a[i])
    maxx = max(max_ending_here,maxx)
    
print(maxx)