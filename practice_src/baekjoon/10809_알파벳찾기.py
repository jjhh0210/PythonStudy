#알파벳 첨등장 하는 위치(포함 안되어있으면 -1)
# s = input()
# answer = [-1 for i in range(26)] #알파벳 개수는 26개~ -1로 초기화
#
# for i in range(len(s)):
#     idx = ord(s[i]) - ord('a')
#     if answer[idx] == -1:       # 처음 등장하는 알파벳만 할당
#         answer[idx] = i
# print(*answer)

###Other### ->파이썬답게 인덱스와 원소를 동시에 접근하면서 루프를 돌리려면?!
s = input()
ck = [-1]*26
n = ord('a')    #97
for i,char in enumerate(s):
    if ck[ord(char) - n] == -1:
        ck[ord(char) - n] = i
print(*ck)