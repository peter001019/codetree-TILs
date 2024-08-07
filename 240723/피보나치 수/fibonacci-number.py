#Top-Down

def fibo(n):
    if memo[n] != -1:
        return memo[n]
    elif n <= 2:
        memo[n] = 1
    else:
        memo[n] =  fibo(n - 1) + fibo(n - 2)
    
    return memo[n]

N = int(input())
memo = [-1] * (N + 1)
print(fibo(N))