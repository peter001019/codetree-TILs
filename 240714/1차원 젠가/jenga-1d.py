n = int(input())
jenga = [int(input()) for _ in range(n)]
temp = []

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

for i in range(len(jenga)):
    if not s1 - 1 <= i < e1:
        temp.append(jenga[i])

jenga = temp.copy()
temp = []

for i in range(len(jenga)):
    if not s2 - 1 <= i < e2:
        temp.append(jenga[i])

jenga = temp.copy()
temp = []

print(len(jenga))
for num in jenga:
    print(num)