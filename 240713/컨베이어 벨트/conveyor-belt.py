n, t = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

for _ in range(t):
    temp1 = list1[n - 1]
    temp2 = list2[n - 1]

    for i in range(n - 1, 0, -1):
        list1[i] = list1[i - 1]
        list2[i] = list2[i - 1]
    
    list1[0] = temp2
    list2[0] = temp1
    
print(*list1)
print(*list2)