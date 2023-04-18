import copy
a = [[-2,2,3],[1,2,9]]
# 2차원 배열의 최대, 최소 구하기!!!
s = min(map(min, a))
e = max(map(max, a))
print(s,e)
b = copy.deepcopy(a)
b[0].append(10)
print(a)
print(b)

# mapp = list(map(int, input()))  #공백없이 한문자기준으로 잘라서 list에 넣음 ex)"123" -> [1,2,3]
# print(mapp)

#뒤 문자 기준 정렬하기
data = ['1 A', '1 B', '6 A', '2 D', '4 B']
data.sort(key = lambda x : (x[-1],x[0]))
print(data)

## Counter
from collections import Counter
lst = ['a','a','b','c','c','c']
counter= Counter(lst)
print(counter)  #딕셔너리형태,
print(counter.most_common()[0][0])  #counter.most_common() : 개수많은거 순으로 튜플로 묶어서 list로반환

##counter 더 살펴보기
counter = Counter("asdffds")
print(counter.most_common())
print(counter.get('f'))
counter['z']=2  #딕셔너리처럼 추가 가능
print(counter.most_common())

##
print(max(1,2,3,4)) #헐~ 인자 반드시 2개가 아녔다

## 최대공약수
import math
print(math.gcd(24,18))