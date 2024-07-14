n, m, t = map(int, input().split())

#상하좌우
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

matrix = [list(map(int, input().split())) for _ in range(n)]
count = [[0] * n for _ in range(n)]
next_count = [[0] * n for _ in range(n)]

def move(x, y): # 큰 곳으로 이동
    max_x, max_y = 0, 0
    for dx, dy in zip(dxs, dys): 
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and matrix[ny][nx] > matrix[y][x]:
            max_x, max_y = nx, ny
                    
    next_count[max_y][max_x] += 1    

def move_all():
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)

for _ in range(m):
    r, c = map(int, input().split())
    count[r - 1][c - 1] += 1

for _ in range(t):
    move_all()
    
    for i in range(n): # 복사
        for j in range(n):
            if next_count[i][j] >= 2:
                next_count[i][j] = 0
            count[i][j] = next_count[i][j]

result = 0

for row in count:
    for n in row:
        if n > 0:
            result += 1
 
print(result)