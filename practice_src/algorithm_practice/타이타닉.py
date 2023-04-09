import sys
from collections import deque
n , m = map(int,sys.stdin.readline().split())
p = list(map(int,sys.stdin.readline().split()))
p.sort()

survived = deque(p) # for popleft()

cnt = 0
while survived:
    remain = len(survived)
    if remain==1:
        cnt+=1
        break       #마지막 한 명 이니까 굳이 pop하지말고 break
    if survived[0] + survived[-1] > m:
        survived.pop() #합이 m보다 크면 맨 뒤에 무거운 애 혼자 타고나가서 혼자 pop
    else:
        # 남은 사람이 한명도 아니고, 양끝 합쳐서 m 이하인 경우 둘이 같이 타고나가니까 둘 다 pop
        survived.pop()
        survived.popleft()
    cnt+=1

print(cnt)