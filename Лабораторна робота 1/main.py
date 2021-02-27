import random
from beautifultable import BeautifulTable
table = BeautifulTable()

a0 = 3
a1 = 4
a2 = 2
a3 = 1

print('Числові значення коефіцієнтів:')
print('a0 =',a0)
print('a1 =',a1)
print('a2 =',a2)
print('a3 =',a3,'\n')

X1 = []
X2 = []
X3 = []

Xn1 = []
Xn2 = []
Xn3 = []

Y = []
Y1 = []
Y2 = []

for i in range(0,8):
    X1.append(random.randint(1, 20))
    X2.append(random.randint(1, 20))
    X3.append(random.randint(1, 20))

print('X1:', X1)
print('X2:', X2)
print('X3:', X3, '\n')

for i in range(8):
    Y.append(a0 + a1*X1[i] + a2*X2[i] + a3*X3[i])

print('Рівняння регресії', '\n'"Y:", Y, '\n')

X01 = (max(X1) + min(X1)) / 2
X02 = (max(X2) + min(X2)) / 2
X03 = (max(X3) + min(X3)) / 2

print('X01 =',X01)
print('X02 =',X02)
print('X03 =:',X03,'\n')

dX1 = X01 - min(X1)
dX2 = X02 - min(X2)
dX3 = X03 - min(X3)

print('dX1 =',dX1)
print('dX2 =',dX2)
print('dX3 =',dX3,'\n')

for i in range(0, 8):
    Xn1.append((X1[i] - X01)/dX1)
    Xn2.append((X2[i] - X02)/dX2)
    Xn3.append((X3[i] - X03)/dX3)

print('Xn1:',Xn1)
print('Xn2:',Xn2)
print('Xn3:',Xn3,'\n')

Y_et = a0 + a1*X01 + a2*X02 + a3*X03

print('Yet =',Y_et)

def average(num):
    Summa = 0
    for i in num:
        Summa = Summa + i
    Summa2 = Summa/8
    return Summa2
r = average(Y)

print('Середнє значення =',r)

for i in range(8):
    f = Y[i] - r
    Y1.append(f)
for l in Y1:
    if l > 0:
        Y2.append(l)
v = r + min(Y2)

print('Результат виконання варіанту:',v)

h0=['№',"X1", "X2", "X3", "Y", "Xn1", "Xn2", "Xn3"]
# table = BeautifulTable()
table.column_headers = h0
for i in range(8):
    h1=[i+1,X1[i], X2[i], X3[i], Y[i], Xn1[i], Xn2[i], Xn3[i]]
    table.append_row(h1)
h3=['X0', X01, X02, X03,'','','','']
h2=['dX', dX1, dX2, dX3,'','','','']

table.append_row(h3)
table.append_row(h2)

print(table)





