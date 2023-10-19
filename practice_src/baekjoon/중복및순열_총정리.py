import sys
from itertools import combinations,permutations,combinations_with_replacement,product
input = sys.stdin.readline

n,m = 4,2
lst = [9, 8, 7, 1]  # 중복 없다는 가정 하에!!!
lst.sort()

'''
group을 [[1,2,3],[2,3,4]]과 같은 형식으로 함
'''

# 5. nPm 순열 (중복x)
print(f"======순열=======")
groups = [list(group) for group in permutations(lst,m)]
print(*groups)

# 6. nCm 조합 (중복x)
print(f"======조합=======")
groups = [list(group) for group in combinations(lst,m)]
print(*groups)

# 7. 중복 허용 순열 == 경우의수 : (상의n개 x 하의m개) 같은 경우의 수 구할 때 good
print(f"======중복 허용 순열=======")
groups = [list(group) for group in product(lst,repeat=2)]
print(*groups)

## 8. 중복 허용 조합
print(f"======중복 허용 조합=======")
groups = [list(group) for group in combinations_with_replacement(lst,m)]
print(*groups)


##########################응용###########################
n,m = 4,2
lst = [9, 7, 9, 1]  # 중복있는 원소 존재 -> 중복된 group 있으면 제거해야 함
lst.sort()

#9. 순열 but [9,1,9,7]처럼 동일한 원소 있는 경우 중복된 경우의 수 제거
print(f"======순열 but 동일 원소 있는 경우=======")
groups = list(permutations(lst, m))
unique_groups = list(set(groups))
unique_groups.sort()
print(*unique_groups)


#10. 조합 but [9,1,9,7]처럼 동일한 원소 있는 경우 중복된 경우의 수 제거
print(f"======조합 but 동일 원소 있는 경우=======")
groups = list(combinations(lst, m))
unique_groups = list(set(groups))
unique_groups.sort()
print(*unique_groups)

#11. 중복 허용 순열 but 동일 원소
print(f"======중복 허용 순열 but 동일 원소 있는 경우=======")
groups = list(product(lst,repeat = 2))
unique_groups = list(set(groups))
unique_groups.sort()
print(*unique_groups)

#12. 중복 허용 조합 but 동일 원소
print(f"======중복 허용 조합 but 동일 원소 있는 경우=======")
cases = list(combinations_with_replacement(lst,m))
unique_cases = list(set(cases))
unique_cases.sort()
print(*unique_cases)