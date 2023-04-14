code = input()

def dfs(d,r):
    global cnt
    if r == "":
        cnt+=1
        print("".join(d))
    else:
        if int(r[0]) > 0:
            d.append(chr(64 + int(r[0])))   # 한자리 1~9 탐색
            dfs(d, r[1:])
            d.pop() # 반드시 탐색 끝나면 원래대로 되돌려줘야!
        if len(r) >=2 and 10<=int(r[:2]) <= 26:    # 두자리가 10~26사이인지 확인
            d.append(chr(64 + int(r[:2])))
            dfs(d, r[2:])
            d.pop()
cnt = 0
d=list()
dfs(d,code)
print(cnt)