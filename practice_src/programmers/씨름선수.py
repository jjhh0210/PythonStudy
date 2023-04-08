import sys
n = int(sys.stdin.readline())
profiles = []
for _ in range(n):
    h,kg = map(int, sys.stdin.readline().split())
    profiles.append((h,kg))

# 키로 내림차순 정렬
profiles.sort(reverse=True)
print(profiles)

# 맨 앞 선수는 이미 모든 사람보다 키 크니 통과
# 두번째 선수부터는 앞의 선수들보다 무조건 몸무게 커야함
cnt = 0
maxx = 0
passed = []
for h, kg in profiles:
    if maxx < kg:
        passed.append((h,kg))
        maxx = kg
        cnt+=1
print(cnt)  #정답!!
print(passed)   # 합격자 확인




