arr = []

def print_answer():
    for e in arr:
        print(e, end=" ")
    print()

def choose(curr_num):
    if curr_num == N + 1:
        print_answer()
        return 
    else:
        for i in range(1, K + 1):
            arr.append(i)
            choose(curr_num + 1)
            arr.pop()

        return

K, N = map(int, input().split())
choose(1)