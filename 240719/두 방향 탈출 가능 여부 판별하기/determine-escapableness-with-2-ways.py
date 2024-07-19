dxs = [0, 1]
dys = [1, 0]

def in_range(x, y):
    return 0 < x <= n and 0 < y <= n

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[y][x] or grid[y][x] == 0:
        return False
    return True

def dfs(x, y):
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if new_x == n and new_y == n:
            return True

        if can_go(new_x, new_y):
            visited[new_y][new_x] = True
            dfs(new_x, new_y)

n , m = map(int, input().split())

grid = [[0] * (n + 1)]
for _ in range(n):
    grid.append([0] + list(map(int, input().split())))
visited = [[False] * (n + 1) for _ in range(n + 1)]

if dfs(1, 1):
    print(1)
else:
    print(0)