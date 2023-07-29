# 양수, +,-
# 식이 최소가 되게 괄호를 치려면 무조건 - 기준으로 항을 나눔 ex) 55 - (50+40) - 60
exp = input()   #식
exp_arr = exp.split("-")            # 1. -로 쪼갬
ans = 0
for i,s in enumerate(exp_arr) :
    if "+" in s:    #식의 형태일 경우
        temp = list(map(int, s.split("+")))     # +가 있으면 더한다
        s = sum(temp)
    else:           # 숫자일 경우
        s = int(s)


    if i == 0:      # 첫번째 원소일 경우
        ans = s
    else:
        ans -=s

print(ans)


### 식을 쪼개서 더하는 법
# exp = "50+30"
# exp_list = list(map(int, exp.split(("+"))))
#
#
# print(sum(exp_list))
