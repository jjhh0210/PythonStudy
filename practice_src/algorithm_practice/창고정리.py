#greedy
import sys
l = int(sys.stdin.readline())
boxes = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())

boxes.sort(reverse=True)

for i in range(m):
    # 변화 : 맨앞-1 맨 뒤+1
    boxes[0]-=1
    boxes[l-1]+=1
    # 맨앞이랑 맨뒤가 각각 최대,최소가 안될경우 sort(정답코드처럼 매번 할 필요는 없을듯)
    if boxes[0]<boxes[1] or boxes[-1]>boxes[-2]:
        boxes.sort(reverse=True)

print(boxes[0]-boxes[-1])
print(boxes)





