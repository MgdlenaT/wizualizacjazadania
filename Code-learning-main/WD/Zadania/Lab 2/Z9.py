# Lab2.Z9
# Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika. 
# Jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.

a = float(input('Podaj liczbe: '))
b = float(input('Podaj stopień pierwiastka, do którego chcesz podniesc te liczbe'))

def spr(a,b):
    c = 1.0 / b # określanie stopnia pierwiastka
    if a<0:
        return 'wylapalem blad' # sprawdzanie bledow
    elif a==0:
        return 0 # wykluczanie 0
    elif a>0:
        i = a**c # podnoszenie liczby użytkownika do potęgi
        return i # zwracanie wyniku

print(spr(a,b)) # wydrukowywanie wyniku