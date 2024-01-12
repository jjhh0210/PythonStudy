'''
가장 많이 주문한 단품 조합
2번 이상 주문되어야 후보가능(1번은 x)
주문수 중복시 둘 다 메뉴o


output :  코스메뉴 오름차순 정렬
'''
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    # 1. course 별로 orders내의 메뉴조합 개수 생성 (with Counter)
    for n in course:  # n = 코스에 들어갈 메뉴 개수
        total_counter = Counter()  # 조합별 주문개수 세야하므로 counter 사용!
        for menus in orders:
            # 메뉴들 알파벳 정렬 -> 그래야 조합도 알파벳 순으로 생성됨
            menus = sorted(menus)
            # 메뉴들 조합 count
            combs = combinations(menus, n)
            temp_counter = Counter(["".join(comb) for comb in combs])  # 튜플 조합 -> 문자열조합으로 변경
            total_counter.update(temp_counter)  # 두 counter 객체 합치기

        # 2. 주문 count가 max인 메뉴들 구하기 (1 이하면 no!)
        if len(total_counter) > 0:
            common_counter = total_counter.most_common()
            max_cnt = common_counter[0][1]
            if max_cnt >= 2:  # 가장 max count값이 2이상이어야함
                for item, cnt in common_counter:
                    # max_cnt보다 작아지는 순간 빠져나옴
                    if cnt < max_cnt:
                        break
                    answer.append(item)

    # 3. answer 오름차순 정렬
    answer.sort()

    return answer