answer = []

def print_answer():
    for e in answer:
        print(e, end=" ")
    print()

def choose(curr_num):
    if curr_num == N + 1:
        print_answer()
        return
    else:
        for i in range(1, K + 1):
            if curr_num <= 2 or (answer[-1] != i or answer[-2] != i):
                answer.append(i)
                choose(curr_num + 1)
                answer.pop()

K, N = map(int, input().split())
choose(1)