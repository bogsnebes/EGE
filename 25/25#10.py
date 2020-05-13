a, b, c, d = [], [], [], []
matrix = [a, b, c, d]
k = -1
u = 0
j = 0
for i in range(4):
    a.append(int(input()))
    b.append(int(input()))
    c.append(int(input()))
    d.append(int(input()))
for i in range(4):
    k += 1
    z = matrix[i]
    j += z[i]
if j % 4 != 0:
    j //= 4
    j += 1
else:
    j //= 4
print('j =', j)
for i in range(4):
    z = matrix[i]
    for k in range(4):
        if z[k] > j:
            print('z[k] =', z[k])
            u += 1
print(u)
