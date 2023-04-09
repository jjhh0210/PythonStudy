from collections import Counter

def solution(gems):
    lt,rt = 0,0
    k = len(set(gems))
    min_len, min_rt, min_lt = float('inf'), 0, 0   #min_len = len(gems)로 초기화하면, 모든 보석원소가 다른 테케에서 if문안에서 min_len, min_rt,min_lt 갱신이 안됨
    counter = Counter()
    for rt in range(len(gems)):
        counter[gems[rt]] += 1
        # 모든 종류가 하나씩 있다면 lt가 쫓아가며 보석 하나씩 빼기 시작
        while len(counter) == k:
            # 가장 짧은 구간 길이인지 확인
            if rt - lt + 1 < min_len:
                min_len = rt - lt + 1
                min_rt = rt + 1
                min_lt = lt + 1
                print(min_rt,min_lt,min_len)

            # lt자리 보석을 counter에서 뺄때, 빼서 0되면 아예 빼고, 그게아니면 -1 해주기
            if counter[gems[lt]]==1:
                counter.pop(gems[lt])
            else:
                counter[gems[lt]] -=1

            lt+=1

    return [min_lt, min_rt]


gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
