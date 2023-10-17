import sys
input = sys.stdin.readline

def solution(n,arr):
    stack = []
    answer = []
    maxx = max(arr)
    point = 0
    for num in range(1,maxx+1):
        stack.append(num)
        answer.append("+")
        while len(stack)>0 and stack[-1]==arr[point]:
            stack.pop()
            answer.append("-")
            point+=1

    while stack:
        if stack[-1] == arr[point]:
            stack.pop()
            answer.append("-")
            point+=1
        else:
            return 0

    return answer


if __name__ == '__main__':
    n = int(input())
    arr = [0]*n
    for i in range(n):
        arr[i] = int(input())
    answer = solution(n,arr)
    if answer==0:
        print("NO")
    else:
        for a in answer:
            print(a)


