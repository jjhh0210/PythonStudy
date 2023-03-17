# import sys
#
# x = sys.stdin.readline().rstrip('\n')
# ten_number = 0
# answer = ''
# for i in range(len(x)):
#     ten_number += int(x[-1])*(2**i)
#     x = x[:-1]
#
# while ten_number != 0:
#     answer += str(ten_number%8)
#     ten_number = ten_number // 8
# print(answer[::-1])

###Other
print(oct(int(input(),2))[2:])