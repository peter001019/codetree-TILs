def initialize():
    for i in range(1, N):
        dp[0][i] += dp[0][i - 1]
    for i in range(1, N):
        dp[i][0] += dp[i - 1][0]

N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

initialize()

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(dp[i - 1][j] + dp[i][j], dp[i][j - 1] + dp[i][j])

print(dp[N - 1][N - 1])