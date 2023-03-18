n = int(input())
ans = ""
#-2진수는 나머지가 -1이나 0이 나올것!!
while n:
    mod = n%(-2)
    if mod: #나머지 -1인경우 -> 사실 우리는 나머지가 1이되게 나눠야하므로 몫에 +1해줘야함
        ans = "1" + ans
        n = (n // -2) + 1
    else:   #나머지 0인 경우
        ans = "0" + ans
        n = n // -2
    # print("{:3d} -> {:2d}".format(n,-mod))
print(ans)
