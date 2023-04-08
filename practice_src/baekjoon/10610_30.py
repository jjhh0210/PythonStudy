## 배수 판정법 -> 3의 배수는 각 자리수의 합이 3의 배수이다

n = list(map(int,input()))
summ = sum(n)
# 각자리 수 합이 3의 배수이고, 0이 있으면(내림차순정렬시 0이 일의자리가 될것)  n은 30의 배수임
if summ%3 == 0 and 0 in n:
    res = sorted(n,reverse=True)    # 정렬
    res = map(str,res)              # 각 원소 int -> str
    print(''.join(res))             # str 타입 list -> 하나의 str으로 결합
else:
    print(-1)
