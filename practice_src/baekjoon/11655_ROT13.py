import sys
s = sys.stdin.readline().rstrip("\n")
answer = ""

for char in s :
    if char.isupper():          #대문자일 때 'A'<= char <='Z'
        i = ord(char) - 65      #A = 65
        char = chr(65+(i+13)%26)
    if char.islower():          #소문자일 때 'a'<= char <='z'
        i = ord(char) - 97      #a = 97
        char = chr(97+(i+13)%26)
    answer+=char
print(answer)
