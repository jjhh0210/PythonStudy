dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, N, M, land_prices, visited, count, total):
    if count == 4:
        return total

    max_price = 0
    for direction in range(4):
        nx, ny = x + dx[direction], y + dy[direction]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            max_price = max(max_price, dfs(nx, ny, N, M, land_prices, visited, count + 1, total + land_prices[nx][ny]))
            visited[nx][ny] = False

    return max_price

def special_case(x, y, N, M, land_prices):
    special_shapes = [
        [(0, 1), (1, 0), (1, 1)],
        [(0, 1), (1, 0), (2, 0)],
        [(0, 1), (0, 2), (1, 1)],
        [(1, 0), (2, 0), (1, 1)]
    ]

    max_special_price = 0
    for shape in special_shapes:
        total = land_prices[x][y]
        valid = True
        for dx, dy in shape:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                total += land_prices[nx][ny]
            else:
                valid = False
                break

        if valid:
            max_special_price = max(max_special_price, total)

    return max_special_price

def max_land_price(N, M, land_prices):
    max_price = 0
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            max_price = max(max_price, dfs(i, j, N, M, land_prices, visited, 1, land_prices[i][j]))
            max_price = max(max_price, special_case(i, j, N, M, land_prices))
            visited[i][j] = False

    return max_price

# 입력 받기
N, M = map(int, input().split())
land_prices = [list(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = max_land_price(N, M, land_prices)
print(result)