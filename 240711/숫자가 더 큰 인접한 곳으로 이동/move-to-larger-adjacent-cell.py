#상하좌우
dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

#r행 c열
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n, r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
r -= 1
c -= 1

def is_move():
    global r, c
    
    print(matrix[r][c], end=' ')

    for i in range(4):
        x = c + dxs[i]
        y = r + dys[i]

        if in_range(x, y) and matrix[y][x] > matrix[r][c]:
            r = y
            c = x

            return True
    return False

while(True):
    if not is_move():
        break