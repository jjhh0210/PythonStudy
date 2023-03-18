a,b = map(int,input().split())
m = int(input())
nums = list(map(int, input().split()))
#a진법->10진법
ten_num = 0
for i in range(len(nums)):
    ten_num += (a**i)*nums[-i-1]

#10진법 -> b진법
ans = ""
while ten_num>0:
    ans = str(ten_num%b)+" "+ans
    ten_num = ten_num//b
print(ans)

