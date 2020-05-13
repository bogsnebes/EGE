#Решение здорового человека
#Python 3.7.0
N = int(input())
School = [0] * 99
Names = [0] * N
number = 0
name = 0
first = True
for i in range(N): # Забитие массива школами.
    a = input()
    a = int(a[-2:])
    School[a] += 1
for i in range(99): # Проверка минимального кол-ва учеников.
    if School[i] > 0:
        if School[i] < School[number] or first:
            first = False
            number = i
name = str(number)
for i in range(99): # Проверка совпадений кол-ва учеников.
    if School[i] == School[number] and i != number:
        name += ', ' + str(i)
print('Минимальное кол-во учеников со школ:', name)
     
    

