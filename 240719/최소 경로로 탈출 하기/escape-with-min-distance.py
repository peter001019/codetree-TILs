from collections import deque

dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

def bfs():
    while q:
        x, y = q.pop()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if in_range(nx, ny) and not visited[ny][nx] and grid[ny][nx] == 1:
                visited[ny][nx] = True
                step[ny][nx] += step[y][x] + 1
                q.appendleft((nx, ny))
        
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * (m) for _ in range(n)]
step = [[0] * (m) for _ in range(n)]
q = deque()

visited[0][0] = True
q.appendleft((0, 0))
bfs()

print(step[n - 1][m - 1] if visited[n - 1][m - 1] else -1)