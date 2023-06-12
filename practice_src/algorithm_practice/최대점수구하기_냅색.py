# 여러번 풀 수 없음 주의 -> 중복 x!!
n,m = map(int, input().split())
dy = [0]*(m+1)  # 시간 = j일 때의 최대 점수!!
for i in range(n):
    score, time = map(int, input().split())
    for j in range(m,time-1,-1):    # 끝에서 부터 time까지 돌아야 함. ex) score = 10. time = 15 이면  m -> 15 까지만 최대 점수를 갱신해야함
        dy[j] = max(dy[j], score+dy[j-time])

print(dy[m])
