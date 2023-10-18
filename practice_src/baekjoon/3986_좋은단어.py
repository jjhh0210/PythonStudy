# 글자수 무조건 짝수여야
# 괄호쌍이랑 똑같음

import sys
input = sys.stdin.readline

def solution(n,words):
    ans = 0 # 좋은단어 수
    stack = []

    for word in words:
        stack.clear()
        # 홀수 단어 거르기
        if len(word)%2 == 1:
            continue
        for ch in word:
            # pop 할 조건
            if stack and stack[-1]==ch:
                stack.pop()
            else: # stack이 0이거나 top이랑 다르면 push
                stack.append(ch)
        # 좋은 단어 : 스택이 비었음
        if not stack:
            ans+=1

    return ans

if __name__ == '__main__':
    n = int(input())
    words = [input().rstrip() for _ in range(n)]
    print(solution(n,words))