dxs = [0, 1]
dys = [1, 0]

def in_range(x, y):
    return 0 < x <= m and 0 < y <= n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[y][x] or grid[y][x] == 0:
        return False
    return True

def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            visited[new_y][new_x] = True
            dfs(new_x, new_y)

n , m = map(int, input().split())

grid = [[0] * (m + 1)]
for _ in range(n):
    grid.append([0] + list(map(int, input().split())))
visited = [[False] * (m + 1) for _ in range(n + 1)]
visited[1][1] = True

dfs(1, 1)

print(1 if visited[n][m] else 0)