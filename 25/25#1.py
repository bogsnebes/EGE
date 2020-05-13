a = []
i = 0
for i in range(30):
    a.append(input(int()))
k = 0
max = 0
dick = True
for k in range(30):
    if (a[k] >= max) or dick:
        max = a[k]
        dick = False
k = 0
for k in range(30):
    if a[k] == max:
        n+=1
print(n)

