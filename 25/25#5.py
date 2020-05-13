a = []
m = []
for i in range(30):
    a.append(int(input()))
for i in range(30):
    if a[i] <= 0:
        m.append(a[i] * (-1))
    else:
        m.append(a[i])
print(*m) 
