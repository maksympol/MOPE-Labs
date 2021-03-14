from random import randint
from math import sqrt
from sys import exit



variant = 322
m = 6
y_max = (30 - variant) * 10
y_min = (20 - variant) * 10
x1_min, x1_max, x2_min, x2_max = 10, 40, 30, 80
x_n = [[-1, -1], [1, -1], [-1, 1]]


def choice_cr():
    table = {5: 2.00, 6: 2.00, 7: 2.17, 8: 2.17, 9: 2.29, 10: 2.29}
    rkr = table.get(m)
    return rkr


def average_y(list):
    aver_y = []
    for i in range(len(list)):
        s = 0
        for j in list[i]:
            s += j
        aver_y.append(s / len(list[i]))
    return aver_y


def dispersion(list):
    disp = []
    for i in range(len(list)):
        s = 0
        for j in list[i]:
            s += (j - average_y(list)[i]) * (j - average_y(list)[i])
        disp.append(s / len(list[i]))
    return disp


def fuv(u, v):
    if u >= v:
        return u / v
    else:
        return v / u


def discriminant(x11, x12, x13, x21, x22, x23, x31, x32, x33):
    return x11 * x22 * x33 + x12 * x23 * x31 + x32 * x21 * x13 - x13 * x22 * x31 - x32 * x23 * x11 - x12 * x21 * x33


y = [[randint(y_min, y_max) for j in range(6)] for i in range(3)]
av_y = average_y(y)
sigma_t = sqrt((2 * (2 * m - 2)) / (m * (m - 4)))
Fuv = []
t = []
Ruv = []
Rkr = choice_cr()

Fuv.append(fuv(dispersion(y)[0], dispersion(y)[1]))
Fuv.append(fuv(dispersion(y)[2], dispersion(y)[0]))
Fuv.append(fuv(dispersion(y)[2], dispersion(y)[1]))
t.append(((m - 2) / m) * Fuv[0])
t.append(((m - 2) / m) * Fuv[1])
t.append(((m - 2) / m) * Fuv[2])

Ruv.append(abs(t[0] - 1) / sigma_t)
Ruv.append(abs(t[1] - 1) / sigma_t)
Ruv.append(abs(t[2] - 1) / sigma_t)


for i in range(len(Ruv)):
    try:
        if Ruv[i] > Rkr:
            print('Помилка, повторіть експеримент')
    except TypeError:
        print("Нестача табличних значень, виберіть корректне m")
        exit()



mx1 = (x_n[0][0] + x_n[1][0] + x_n[2][0]) / 3
mx2 = (x_n[0][1] + x_n[1][1] + x_n[2][1]) / 3
my = (av_y[0] + av_y[1] + av_y[2]) / 3

a1 = (x_n[0][0] ** 2 + x_n[1][0] ** 2 + x_n[2][0] ** 2) / 3
a2 = (x_n[0][0] * x_n[0][1] + x_n[1][0] * x_n[1][1] + x_n[2][0] * x_n[2][1]) / 3
a3 = (x_n[0][1] ** 2 + x_n[1][1] ** 2 + x_n[2][1] ** 2) / 3

a11 = (x_n[0][0] * av_y[0] + x_n[1][0] * av_y[1] + x_n[2][0] * av_y[2]) / 3
a22 = (x_n[0][1] * av_y[0] + x_n[1][1] * av_y[1] + x_n[2][1] * av_y[2]) / 3

b0 = discriminant(my, mx1, mx2, a11, a1, a2, a22, a2, a3) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b1 = discriminant(1, my, mx2, mx1, a11, a2, mx2, a22, a3) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b2 = discriminant(1, mx1, my, mx1, a1, a11, mx2, a2, a22) / discriminant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)

y_pr1 = b0 + b1 * x_n[0][0] + b2 * x_n[0][1]
y_pr2 = b0 + b1 * x_n[1][0] + b2 * x_n[1][1]
y_pr3 = b0 + b1 * x_n[2][0] + b2 * x_n[2][1]

dx1 = abs(x1_max - x1_min) / 2
dx2 = abs(x2_max - x2_min) / 2
x10 = (x1_max + x1_min) / 2
x20 = (x2_max + x2_min) / 2

koef0 = b0 - (b1 * x10 / dx1) - (b2 * x20 / dx2)
koef1 = b1 / dx1
koef2 = b2 / dx2

yP1 = koef0 + koef1 * x1_min + koef2 * x2_min
yP2 = koef0 + koef1 * x1_max + koef2 * x2_min
yP3 = koef0 + koef1 * x1_min + koef2 * x2_max

print('Матриця планування для m =', m)
print(y[0])
print(y[1])
print(y[2], "\n")

print('Експериментальні значення критерію Романовського:')
print(Ruv[0])
print(Ruv[1])
print(Ruv[2], "\n")

print('Натуралізовані коефіцієнти: \na0 =', round(koef0, 4), 'a1 =', round(koef1, 4), 'a2 =', round(koef2, 4), "\n")
print('У практичний ', round(y_pr1, 4), round(y_pr2, 4), round(y_pr3, 4),
      '\nУ середній', round(av_y[0], 4), round(av_y[1], 4), round(av_y[2], 4))
print('У практичний норм.', round(yP1, 4), round(yP2, 4), round(yP3, 4))