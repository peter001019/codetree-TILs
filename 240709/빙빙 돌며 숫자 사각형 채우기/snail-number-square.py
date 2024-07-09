n, m = map(int, input().split())
matrix = [ 
    [0] * m #앞에가 열 
    for _ in range(n)
]

x, y = 0, 0
move_dir = 0

#동 남 서 북
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < m and 0 <= y < n

for num in range(1, n * m + 1):
        matrix[y][x] = num

        dx = x + dxs[move_dir]
        dy = y + dys[move_dir]

        if not in_range(dx, dy) or matrix[dy][dx] != 0: # 갈 곳이 없으면 90도 회전
            move_dir = (move_dir + 1) % 4
        
        x += dxs[move_dir]
        y += dys[move_dir]

for row in matrix:
    print(*row)