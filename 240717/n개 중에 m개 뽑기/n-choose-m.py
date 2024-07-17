arr = []

def choose(curr_num, num):
    if curr_num == M + 1:
        print(*arr)
        return
    
    for n in range(num, N + 1):
        arr.append(n)

        choose(curr_num + 1, n + 1)

        arr.pop()

N, M = map(int, input().split())
choose(1, 1)