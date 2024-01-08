'''
>입력
- 소문자, 1개 이상의 모음, 2개 이상의  자음
- 알파벳 무조건 증가 순서
L암호길이(중복x), C종류알파벳

>출력
사전순으로 모든 가능한 암호 출력

-> 중복 없이 순열 (cPl+ 조건)
'''

import sys
input = sys.stdin.readline
l, c = map(int, input().split())
words = sorted(input().split()) # 알파벳 순 정렬
ans = []
word = [None]*l   # 현재 만들고 있는 단어
def dfs(depth,s):
    # print(depth,":",word)
    if depth == l:
        # 모음 개수, 자음 개수 구하기
        mo = sum(1 for ch in word if ch in 'aeiou')
        ja = l-mo
        # 모음,자음 개수 조건 충족시
        if mo >=1 and ja>=2:
            ans.append(''.join(word))
        return
    else:
        for i in range(s,c):
            word[depth] = words[i] # 현재 단어에 추가
            dfs(depth+1, i+1)
            # word[depth] = None

dfs(0,0)

for w in ans:
    print(w)
