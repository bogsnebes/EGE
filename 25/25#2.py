a = []
i = 0
for i in range(0, 30):
    print("Ваше число в ", i, ": ")
    a.append(int(input()))
i = 0
maxsum = 0
n = 0
ass = True
for i in range(28):
    n = a[i] + a[i+1] + a[i+2]
    if n > maxsum or ass:
        maxsum = n
        ass = False
print(maxsum)