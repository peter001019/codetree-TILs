n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 동 남 서 북
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
result = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for x in range(n):
    for y in range(n):
        count = 0

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and matrix[nx][ny] == 1:
                count += 1
        
        if(count >= 3):
            result += 1

print(result)