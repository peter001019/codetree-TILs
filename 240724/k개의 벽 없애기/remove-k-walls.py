from collections import deque
import sys, copy

#동서남북
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(ngrid, visited):
    while q:
        x, y = q.pop()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and ngrid[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                ngrid[ny][nx] = ngrid[y][x] + 1
                q.appendleft((nx, ny))

def choose(curr_num, num): #block 배열에서 없애야할 벽을 선택
    if curr_num == k:
        return execute()
    
    for n in range(num, len(block)):
        arr.append(block[n])
        choose(curr_num + 1, num + 1)
        arr.pop()

def execute(): #선택된 벽을 없애고, bfs를 실행한다.
    global result
    ngrid = copy.deepcopy(grid)
    visited = [[False] * n for _ in range(n)]
    end_x, end_y = end[1] - 1, end[0] - 1

    for x, y in arr:
        ngrid[y][x] = 0

    q.append((start[0] - 1, start[1] - 1))
    bfs(ngrid, visited)

    if visited[end_y][end_x] and result > ngrid[end_y][end_x]:
        result = ngrid[end_y][end_x]

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
q = deque()
block = []

for i in range(n): # 장애물 탐색
    for j in range(n):
        if grid[i][j] == 1:
            block.append((j, i))
arr = []
result = sys.maxsize

choose(0, 0)

print(result)

'''
k개의 벽을 선택한다.

선택된 벽을 없애고, bfs를 실행한다. 그러면 도착지에 최소시간이 나온다.

나온 최소 시간이 현재 최소값보다 작다면 값을 바꾼다.

최소값을 출력한다.

visited배열의 도착 지점 값을 확인해서 도착여부를 확인한다.
도착 했다면 최소 시간 출력
'''