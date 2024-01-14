def solution(plans):
    answer = []  # 과제 끝낸 순서대로 이름 return
    posed = []  # 멈춘

    def convert_to_minutes(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m

    # 배열의 시간 변경 + 시작시간순 정렬
    plans = [[name, convert_to_minutes(start), int(duration)] for name, start, duration in plans]
    plans.sort(key=lambda x: x[1])

    name, st, pt = plans[0]  # 현재 과제
    for i in range(1, len(plans)):
        nname, nst, npt = plans[i]  # 다음과제

        # 다음 시작시간이 현재 작업 끝나는 시간보다 작으면
        if nst < st + pt:
            # 현재꺼 멈춤, 다음게 현재 작업됨
            posed.append([name, st + pt - nst])  # 과제, 남은playtime
            name, st, pt = nname, nst, npt
        # 크거나 같으면
        else:
            # 현재 작업 끝 + 남는 시간만큼 멈췄던 애들 수행
            answer.append(name)
            st += pt  # 현재 시간 갱신
            while nst > st and posed:  # 다음과제시작이 현재시각보다 클동안만 남은 과제 수행
                posed_name, posed_pt = posed[-1][0], posed[-1][1]
                if posed_pt <= nst - st:
                    # 남은과제 끝
                    answer.append(posed_name)
                    st += posed_pt
                    posed.pop()
                else:
                    posed[-1][1] = posed_pt - (nst - st)
                    st = nst
                # print(posed)
            name, st, pt = nname, nst, npt

    # 마지막 과제와 posed에 남은 과제 처리
    answer.append(name)
    while posed:
        answer.append(posed.pop()[0])

    return answer