N, M = map(int, input().split())

matrix = [[0] * N for _ in range(N)]

#동서남북
dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def is_comfort(x, y):
    count = 0

    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]

        if in_range(nx, ny) and matrix[ny][nx] == 1:
            count += 1
    
    return count == 3


for _ in range(M):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    matrix[r][c] = 1

    if is_comfort(c, r):
        print(1)
    else:
        print(0)