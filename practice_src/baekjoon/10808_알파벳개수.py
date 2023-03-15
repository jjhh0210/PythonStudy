# s = input()
# n = ord('z')-ord('a') +1    #총 알파벳 개수
# #print(n) #26개!
# answer = [0 for i in range(n)]  #a~z개수 담을 배열 0으로 초기화
# for char in s :
#     idx = ord(char) - ord('a')
#     answer[idx]+=1
# print(*answer)     # *붙이면 리스트 대괄호 없이 한번에 출력!아니면 for문안에서 print(x,end=' ')..


###Other### ->사실상 같은코드
s = input()
cnt = [0]*26
n = ord('a')    #97
for char in s:
    cnt[ord(char) - n]+=1
print(*cnt)