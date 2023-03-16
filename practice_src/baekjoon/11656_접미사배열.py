import sys
s = sys.stdin.readline().rstrip("\n")
ans = []

# for i in range(len(s)):
#     ans.append(s[i:])

for _ in s:
    ans.append(s)
    s = s[1:]

ans.sort()
print(*ans,sep='\n')    #구분자를 요소들 사이에 출력 가능 (기본은 공백)

