def choose(curr_num):
    if curr_num == n + 1:
        print(*arr)

    else:
        for num in range(1, n + 1):
            if visited[num]:
                continue
            visited[num] = True
            arr.append(num)
            choose(curr_num + 1)
            
            arr.pop()
            visited[num] = False

n = int(input())
visited = [False for _ in range(n + 1)]
arr = []

choose(1)