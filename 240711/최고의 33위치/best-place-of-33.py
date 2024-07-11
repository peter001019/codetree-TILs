N = int(input())
matrix = []
count = 0

for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

def count_one(x, y):
    count = 0

    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if(matrix[i][j] == 1):
                count += 1

    return count

for i in range(N - 2):
    for j in range(N - 2):
        new_count = count_one(i, j)

        if count <= new_count:
            count = new_count

print(count)