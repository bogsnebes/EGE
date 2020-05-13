a = []
n = 1000
for i in range(n):
    a.append(int(input()))
m = 10000
k = 10000
for i in range(n):
    if a[i] % 3 == 0 and a[i] < m:
        m = a[i]
    elif a[i] % 5 == 0 and a[i] < k:
        k = a[i]
for i in range(n):
    if a[i] % 15 == 0:
        a[i] -= m + k
    elif a[i] % 3 == 0:
        a[i] -= m
    elif a[i] % 5 == 0:
        a[i] -= k
print(*a)
