 # Lab2.Z8
# Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, 
# następnie dodaje do listy tylko parzyste liczby.

a = 10 # określanie ilości liczb

fullist = [] # Tworzenie 
list = []    # Pustych List

while a > 0:
    i = int(input('podaj liczbe: '))  # Pobieranie Liczb
    fullist.append(i)                 # Dodawanie ich do pełnej listy
    if i % 2 == 0:                    # Sprawdzanie czy liczba jest parzysta
        list.append(i)                # Dodawanie parzystej liczby do mniejszej listy
    a = a-1                           # Zmniejszanie ilości pozostałych liczb przy każdym powtórzeniu pętli

print('pelna lista: ')      # Zwracanie losty wszystkich pobranych liczb
for x in fullist[::1]:
    print(x)

print('lista z tylko parzystymi liczbami: ')    # Zwaracanie listy tylko z parzystymi liczbami
for x in list[::1]:
    print(x)