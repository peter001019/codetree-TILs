x, y = 0, 0
move = str(input())

#동, 남, 서, 북
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dir = 3

for s in move:
    if s == 'F':
        x += dx[dir]
        y += dy[dir]
    elif s == 'L':
        dir = (3 + dir) % 4
    else:
        dir = (dir + 1) % 4

print(str(x) + " " + str(y))