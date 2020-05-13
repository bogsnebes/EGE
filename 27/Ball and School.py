# Python 3.7.0
"""
Вход:
N - кол-во учеников
Фамилия, имя, школа и балл - отсеить Фамилию и имя.
Значение школ варируется от 1 до 99.
Баллы от 0 до 100.

Выход:
Номер школы, где максимальное количество школьников с макс. баллами.
Если кол-во учеников у школ совпдает, то вывести оба.
"""
N = int(input())
school = [0] * 98
ball = 0
data = 0
max_ball = 0
last_school = 0
king = 0
first = True
for i in range(N):
    data = input()
    ball = int(data[-3:])
    data = int(data[-5:-3])
    print(data)
    if ball > max_ball or first: # Проверка максимального балла.
        max_ball = ball
        school.clear()
        school = [0] * 98
        school[data] += 1
        first = False
        last_school = data
    elif ball == max:
        school[data] += 1
    if data != last_school:
        if school[last_school] > school [data]: # Выявление короля.
            king = last_school
        elif school[data] > school [last_school]:
            king = data
        else: # school[last_school] = school [data]
            king = str(data) + ' ,' + str(last_school)
    else:
        king = data
print('Учеников с максимальным баллом больше всего со школ:', king)
