n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

#1. sort
seq.sort()

#2. 양수 음수 나누기
pos = []
neg = []
i=0
if len(seq)==1:
    print(seq[0])
else:
    for i in range(len(seq)):       # 원소 1개일때 range(0,0)돼서 반복문이 안돌아가므로 따로 빼줘야 함
        if seq[i] > 0:
            neg.extend(seq[0:i])    # 0 ~ i까지 음수들(0포함)
            pos.extend(seq[i:])   # i ~ 끝까지 양수들 -> 내림차순정렬
            break
    pos.sort(reverse=True)  #양수는 내림차순으로 정렬 후 큰수부터 묶어줘야함
    # 음수일때
    sum_neg = 0
    sum_pos = 0
    for i in range(0,len(neg),2):
        if i+1 >= len(neg): # 개수가 홀수일 때 마지막 한개 남은 것은 그냥 더해줌
            sum_neg += neg[i]
        else:
            sum_neg += neg[i]*neg[i+1]  #두개 곱해서 더하기
    # 양수일 떄
    for i in range(0,len(pos),2):
        #
        if i+1 >= len(pos): # 개수가 홀수일 때 마지막 한개 남은 것은 그냥 더해줌
            sum_pos += pos[i]
        elif pos[i+1] == 1: # i+1 수가 1일경우
            sum_pos += pos[i]+pos[i+1]  #각각 더하기
        else:
            sum_pos += pos[i]*pos[i+1]  #두개 곱해서 더하기

    print(sum_pos+sum_neg)