import sys
sys.setrecursionlimit(10**4)

#동서남북
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < M and 0 <= y < N

def dfs(x, y, colored):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and not colored[ny][nx]:
            colored[ny][nx] = True #방문한 곳 색칠 표시
            dfs(nx, ny, colored)

def simulation(K):
    safety = 0
    colored = [[False] * M for _ in range(N)]

    for i in range(N): # 침수되면 색칠
        for j in range(M):
            if grid[i][j] <= K:
                colored[i][j] = True
    
    for i in range(N): #색칠 안된 영역에 대해 dfs
        for j in range(M):
            if not colored[i][j]:
                safety += 1
                dfs(j, i, colored)
    
    return safety

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

max_K = 1
max_safety = 0

for k in range(1, 100):
    safety = simulation(k)
    if safety > max_safety:
        max_K = k
        max_safety = safety

print(max_K, max_safety)

#K에 맞게 색칠을 한다.
#색칠 안된 영역에서 dfs를 해본다. -> 이때 색칠 안된 곳이면 안전영역 수를 늘린다.
#저장하고, 안전영역이 크다면 바꾼다.(같으면 안바꿈)