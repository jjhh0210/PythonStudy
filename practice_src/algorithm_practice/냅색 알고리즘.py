n,m = map(int, input().split()) # 보석 개수, 무게 제한
dy = [0]*(m+1)  # 무게한계 = j 일때의 최대 보석 가치

for i in range(n):
    w,v = map(int, input().split())
    for j in range(w,m+1):
        dy[j] = max(dy[j], dy[j-w]+v)   # 담지 않은 기존값, 현재 보석을 담았을 떄 값

print(dy[m])



