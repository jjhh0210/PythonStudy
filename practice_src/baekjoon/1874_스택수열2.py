import sys
input = sys.stdin.readline
def solution(n,seq):
    k = 0   # 1~n까지의 자연수 (0으로 해야 첫번째 숫자 1이 될 때까지 while 루프 적어도 한번 실행됨)
    stack = []
    ans = []

    for num in seq:
        while k < num:  # 수열 원소보다 k가 작은 애들 모두 stack에 push
            k+=1
            stack.append(k)
            ans.append("+\n")

        # k>=num
        # num과 stack의 마지막이 같다면
        if num==stack[-1]:
            stack.pop()
            ans.append("-\n")
        else:
            return "NO"

    return ans

if __name__ == '__main__':
    n = int(input())
    seq = [int(input()) for _ in range(n)]
    ans = solution(n,seq)
    if ans =="NO":
        print("NO")
    else:
        print(''.join(ans))
