s,b = input().split()
b = int(b)
n = 0
while s:
    k = s[0]
    n = b*n+(int(k) if k.isdigit() else (ord(k)-65+10))
    s = s[1:]
print(n)

###Other
# tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# while s :
#     k = s[0]
#     n = b*n+int(tmp.find(k)) #문자열에서 문자 인덱스 찾기 : tmp.find(k), tmp.index(k)
#     s=s[1:]
#print(n)
