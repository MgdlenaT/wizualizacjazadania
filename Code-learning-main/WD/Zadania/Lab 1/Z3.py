# Lab1.Z3
# Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %

# Pobieranie danych od użytkownika:
a = int(input('podaj pierwsza cyfre: '))
b = int(input('podaj druga cyfre: '))

# Operator przyrostkowy dla dodawania:
def  dodawanie(j,i):
    print('dodawanie: ', j+i)

# Operator przyrostkowy dla odejmowania:
def odejmowanie(j,i):
    print('odejmowania: ', j-i)

# Operator przyrostkowy dla mnożenia:
def mnozenie(j, i):
    print('mnozenie: ', j*i)
    
# Operator przyrostkowy dla dzielenia:
def dzielenie(j,i):
    print('dzielenie: ', j/i)

# Operator przyrostkowy dla potęgowania:
def potega(j,i):
    print('potega: ', j**i)

# Operator przyrostkowy dla reszty:
def reszta(j,i):
    print('reszta: ', j%i)

# Wydrukowanie wszystkich operatorów przyrostkowych i ich wyników:
print(dodawanie(a,b), odejmowanie(a,b), mnozenie(a,b), dzielenie(a,b), potega(a,b), reszta(a,b))