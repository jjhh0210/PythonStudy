'''
다음 달에 누가 선물을 많이 받을지 예측
- 주받 O -> 더 준사람이 1개 받음
- 주받 X or 수 같음 -> 선물 지수가 더 큰 사람이 1개 받음
    - 선물지수 : 총 준선물-받은선물 (얼마나 퍼줬나)
    - 선물지수도 같으면 주고받지 x

입력
- friens: 친구들 이름
- gifts: ["준애 -> 받은애",...]
출력: 가장 많은 선물 받을 친구의 선물 수
'''


def solution(friends, gifts):
    answer = 0
    n_friends = len(friends)
    # 친구 인덱스 dict 생성
    index = dict()
    for i, friend in enumerate(friends):
        index[friend] = i
    # 친구별 다음 달에 받을 선물개수
    next_gift = [0] * n_friends

    # 1. 선물 행렬 만들기
    mapp = [[0] * (n_friends + 1) for _ in range(n_friends + 1)]  # 마지막 원소는 sum
    for gift in gifts:
        give, take = gift.split()
        mapp[index[give]][index[take]] += 1
    # 각 행/열의 마지막 원소 - 전체 주고받은 선물
    for i in range(n_friends):
        mapp[i][-1] = sum(mapp[i][:])
        mapp[-1][i] = sum(mapp[j][i] for j in range(n_friends))

    # 2. 선물 받을 사람 알고리즘
    for i in range(n_friends):
        for j in range(i + 1, n_friends):  # 둘 관계 중복 피하기 위해 i+1부터!
            # 서로 주고 받았음 + 그 수가 같지 않음 -> 선물지수 계산x
            # i=준사람, j =받은사람, ij:준갯수 ji=받은개수
            if mapp[i][j] != mapp[j][i] and (mapp[i][j] > 0 or mapp[j][i] > 0):
                max_idx = i if mapp[i][j] > mapp[j][i] else j  # 둘 중 더 준사람 찾기
                next_gift[max_idx] += 1  # 더 준사람이 1개 더 받음

            # 그 외 경우 -> 선물지수 계산
            else:
                # 선물지수 : 준sum-받은sum
                diff_i = mapp[i][-1] - mapp[-1][i]
                diff_j = mapp[j][-1] - mapp[-1][j]

                if diff_i != diff_j:
                    max_idx = i if diff_i > diff_j else j  # 둘 중 선물 지수 큰사람 찾기
                    next_gift[max_idx] += 1  # 둘 중 선물지수 더 큰 사람이 1개 더 받음

    answer = max(next_gift)
    return answer