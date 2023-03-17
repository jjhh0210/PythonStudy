n,b = map(int,input().split())
ans = ""
while n>0:
    mod = n%b
    ans = (str(mod) if mod < 10 else chr(65+mod-10))+ans
    n = n//b
print(ans)
