""" Вход:
    N < 3000
    Курс биткоинов каждый N день.
    
    Выход:
    Максимальная выручка, день закупки, день продажи
"""
N = int(input())
curs = 0
first_min = True
min = 0
min2 = 0
den_min = 0
den_max = 1
den_min_2 = 0
max = 0
max2 = 0
jackjack = 0
for i in range(1, N+1):
    curs  = int(input())
    if i != 1 and curs > max:
        max2 = max
        max = curs
        den_max = i
    if curs < min or first_min:
        if den_max >= den_min:
            jackjack = 0
        if den_max < i and jackjack != 1 or first_min:
            min2 = min
            if den_min == 0:
                den_min_2 = 1
            else:
                den_min_2 = den_min
            jackjack = 1
        first_min = False
        min = curs
        den_min = i
    if den_max >= den_min and curs - min > max - min2:
        max = curs
        den_max = i
        here = 0
    elif den_max <= den_min:
        here = 1
if here == 1:
    print(max - min2, den_min_2, den_max)
elif here == 0:
    print(max-min, den_min, den_max)
