import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)


def solution(maps):
    answer = []
    rowN = len(maps)
    colN = len(maps[0])

    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    board = [list(string) for string in maps]

    def dfs(ci, cj):
        # 초기화
        nonlocal summ
        summ += int(board[ci][cj])
        board[ci][cj] = "X"

        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            # OOB가 아니고, X가 아니면 탐색
            if 0 <= ni < rowN and 0 <= nj < colN and board[ni][nj] != "X":
                dfs(ni, nj)

    for i in range(rowN):
        for j in range(colN):
            # 무인도 탐색
            if board[i][j] != "X":
                summ = 0
                dfs(i, j)
                answer.append(summ)

    # answer 길이 0이면 [-1]
    if not answer:
        return [-1]

    return sorted(answer)