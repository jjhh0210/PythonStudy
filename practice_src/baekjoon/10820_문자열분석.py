#문자열들의 소문자, 대문자, 숫자, 공백 개수
import sys
#빈문자열 입력시 stop
while True:
    s = sys.stdin.readline().rstrip('\n')
    # s = input()          #input으로 하면 오류남..ㅠㅠ
    if not s :      #빈문자열 입력시 break
        break
    a,b,c,d = 0,0,0,0
    for char in s:
        if char.islower():  #소문자개수
            a+=1
        elif char.isupper():  #대문자개수
            b+=1
        elif char.isdigit():    #숫자개수
            c+=1
        elif char.isspace():       #나머지는 공백
            d+=1
    print(a,b,c,d)
