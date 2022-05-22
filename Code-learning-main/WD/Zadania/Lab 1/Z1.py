# Zadanie Nr1.
#Napisz pierwszy skrypt, w ktorym zadeklarujesz zmienne każdego typu, a następnie wyświetl te zmienne.

# Zmienne typu int:
a = 1
b = 2

# Zmienne typu Float
c = 3.14
d = 5.17

# Zmienne typu String:
e = 'ab'
f = 'cd'

# Zmienne typu Boolean:
g = False
h = True

# Zmienne typu None:
i = None

# Zmienne typu Kolekcja:

# 1: Lista:
j = [1,2,3,4,5,6,7,8,9,0]
k = [a,b,c,d,e,f,g,h,i,j]

# 2: Tupla:
l = (1,2,3,4,5,6,7,8,9,0)
m = (a,b,c,d,e,f,g,h,i,j)

# 3: Slownik:
n = {
    'a' : 1,
    'b' : 2,
    'c' : 3}
o = {
    1 : 'a',
    2 : 'b',
    3 : 'c'}

# Zmienne typu funkcja:
def p(x,y):
    z = x + y 
    return z
def q(x,y):
    z = x - y
    return z

# Zwrocenie i wydrukowanie wszystkich zmiennych:
print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p(a,b), q(a,b))