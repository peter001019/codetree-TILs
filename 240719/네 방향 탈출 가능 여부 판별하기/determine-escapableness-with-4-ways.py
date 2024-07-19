from collections import deque

#상하좌우
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def bfs():
    while q:
        curr = q.pop()

        for dx, dy in zip(dxs, dys):
            nx, ny = curr[0] + dx, curr[1] + dy

            if in_range(nx, ny) and grid[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.appendleft((nx, ny))

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
q = deque()

q.appendleft((0, 0))
visited[0][0] = True
bfs()

print(1 if visited[n - 1][m - 1] else 0)