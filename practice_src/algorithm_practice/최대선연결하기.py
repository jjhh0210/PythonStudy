## 최대부분증가수열 문제와 같음
## 역추적을 통해 수열 출력해보기
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dy = [0]*(n+1)  #메모이제이션
prev = [0]*(n+1)  # 이전 위치 기록
dy[1] = 1
res = 0
last_index = 0  # 최대 부분 증가수열의 마지막 위치

for i in range(2,n+1):
    max_val = 0
    for j in range(i-1,0,-1):
        if arr[j] < arr[i] and dy[j]>max_val:
            max_val = dy[j]
            prev[i] = j  # j 위치에서 i로 왔다고 기록
    dy[i] = max_val+1
    # 최대증가수열의 길이
    if dy[i]>res:
        res = dy[i]
        last_index = i  # 최대 길이가 갱신되면 마지막 위치 갱신

# 최대 부분 증가수열 추출
seq = []
while last_index != 0:
    seq.append(arr[last_index])
    last_index = prev[last_index]  # 이전 위치로 이동
seq.reverse()  # 역순으로 얻었으므로 뒤집기

print(res)
print(' '.join(map(str, seq)))
print(prev)