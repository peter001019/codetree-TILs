import sys

N = int(sys.stdin.readline())
x, y = 0, 0
dx = {'W': -1, 'S': 0, 'N': 0, 'E': 1}
dy = {'W': 0, 'S': -1, 'N': 1, 'E': 0}

for _ in range(N):
    direct, move = sys.stdin.readline().split()
    x += int(move) * dx[direct]
    y += int(move) * dy[direct]

print(str(x) + " " + str(y))