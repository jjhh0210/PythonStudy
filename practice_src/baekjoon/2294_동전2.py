'''
<조건>
- n가지 종류의 동전이 있다. 이 동전들을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그러면서 동전의 개수가 최소가 되도록 하려고 한다.
- 각각의 동전은 몇 개라도 사용할 수 있다.
- 가치가 같은 동전이 여러 번 주어질 수도 있다. -> 같으면 넘어가도 될덧..?
- 사용한 동전의 최소 개수를 출력한다. 불가능한 경우에는 -1을 출력

<input>
3 15    # n종류, k원
5
3
12

<output>
2
-------------------------------------
d[i][j] = i에 대해 j원까지 만드는데 필요한 최소 개수

    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
0   0 - - - ~~~~   (-1로 초기화)
5   0 - - - -[1 - - - - 2   -  -  -  -  3]
3   0 - -[1 - 1 2 - 2 3 2   -  4  3  -  3] (5 vs 3)
12  0 - - 1 - 1 2 - 2 3 2   - [1  3  -  2] (3 vs 2 -->12+3)


d[j] = d[j] vs d[j-coin]+1 인데...
1) d[j] or d[j-coin] 중 하나라도 -1이면 무조건 둘 중 자연수!!!(max)
2) 둘 다 -1이 아니면 둘 중 작은거 (min)
'''

import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coins = set()
for _ in range(n):
    coin = int(input())
    coins.add(coin)

### -1로 초기화 했을 때
# d = [-1]*(k+1)
# d[0]=0

# for coin in coins:
#     for j in range(coin, k+1):
#         if d[j]<0 or d[j-coin]<0:
#             d[j] = max(d[j], d[j-coin]+1)
#             if d[j]==0: d[j]=-1
#         else:
#             d[j] = min(d[j], d[j-coin]+1)

### 10001 (max)값으로 초기화 했을 때
d = [10001]*(k+1)
d[0]=0

for coin in coins:
    for j in range(coin, k+1):
        d[j] = min(d[j],d[j-coin]+1)

if d[k]==10001:
    print(-1)
else:
    print(d[k])