def dfs(vertex):
    global count

    for nxt in graph[vertex]:
        if visited[nxt]:
            continue
        count += 1
        visited[nxt] = True
        dfs(nxt)
        

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
visited[1] = True
count = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
print(count)