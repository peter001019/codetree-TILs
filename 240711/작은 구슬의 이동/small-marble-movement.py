n, t = map(int, input().split())
r, c, d = input().split()
r = int(r)
c = int(c)

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

#동 남 북 서
mapper = {
    'R': 0,
    'D': 1,
    'U': 2, 
    'L': 3
}

dxs = [1, 0, 0, -1]
dys = [0, 1, -1, 0]
move_dir = mapper[d]

for _ in range(t):
    nc = c + dxs[move_dir]
    nr = r + dys[move_dir]

    if in_range(nc, nr):
        c = nc
        r = nr
    else:
        move_dir = 3 - move_dir

print(str(r) + " " + str(c))