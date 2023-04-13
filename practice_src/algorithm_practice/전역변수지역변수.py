
# def sol(a):
#     global n    # n은 무조건 전역변수로 써라!
#     if n==1:
#         n=n+3    #여기서 interpreter가 새로운 지역변수 n을 만든다고 해석, 그럼 이 함수에서의 n은 local 변수화 된거임!! 그러므로 먼저 n==1에서 에러남
#         print(n,lst)
#     lst[0] = 9  # 이거는 로컬 lst변수를 새로 생성하는게 아니기 땜에 자동으로 전역변수로 인식. 기존 값을 변경하는 정도이므로 에러 x.
#     # lst =  lst+[3] # 새로운 lst 생성한다고 해석 -> 지역변수화 -> 하므로 에러 -> lst 지역변수가 없는데 더하려 하고 있음 있음
#     a+=1
#     print(a)    #4

# 파이썬은 전역변수 검색하는것보다 지역변수 검색하는게 빠르다함!
answer = 0
A = []
B = 0
C = 0
def sola():
    global answer,A,B,C
    cnt = 1
    if answer < 3:
        cnt+=1
        A.append('a')
        B+=1
        C+=1

    return cnt

def solution(a,b,c):
    A = a
    B = b
    C = c
    print(sola())
    print(A,B,C)
    return answer

if __name__ == '__main__':
    n = 1
    lst = [1,2,3]
    a=3
    print(solution(lst,n,a))
