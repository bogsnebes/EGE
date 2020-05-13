#Волосатый чипобряк
#Python 3.7.0
""" Гоночная трасса состоит из двух основных дорог и 
    нескольких переездов, позволяющих перейти с одной дороги на другую.

    - Движение в одну сторону (только с А в В)
    - Старт с А0, финиш ВN
    - Известно t для движения горизонтально и вертикально,
                                    оно может различаться.
    - Найти минимальное t (всего пути)

    - Обозначать А = 0, В = 1 (here)
    - Cкладывать А, найти точку где оно становится больше В (с учетом)
                                                    вертикального пути.
    - Если Distance_A > Distance_B 
    
"""
N = int(input())
Time_vertical = int(input())
All_Time = Time_vertical
Distance_A = 0
Distance_B = 0
here = 0
Size = 0
A1 = 0 
B1 = 0
first = True
for i in range(N):
    A1 = int(input())
    B1 = int(input())
    Distance_A += A1
    Distance_B += B1
    print('Distance:', Distance_A)
    if Distance_A + Time_vertical > Distance_B and here != 1 or first: # Проверка поворота.
        All_Time = Distance_A - A1 + B1 + Time_vertical 
        here = 1
        first = False
        print('1')
    elif Distance_A + Time_vertical < Distance_B:
        here = 0
        print('2')
    elif here == 1:
        All_Time += B1
        print('3')
    if i == N - 1 and here == 0:
        All_Time = Distance_A + Time_vertical
        print('4')
print("Время прохождения пути:", All_Time)
# Distance_A > Distance_A - A[i] + B[i] + Time_vertical
