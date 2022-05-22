# Lab2.Z5
# Napisz skrypt gdzie pobierzesz trzy liczby całkowite, 
# gdzie wykonasz obliczenia: a**b + c.
# Użyj instrukcji readline() i write()).

i = input('Podaj 3 liczby calkowite, oddzielajac je spacja: ') # Pobieranie trzech liczb od urzytkownika 

f = open("myfile.txt", "w")    # Tworzenie pliku 'myfile.txt' i wpisanie do niego trzech liczb
f.write(i)

f = open("myfile.txt", "r")             # otworzenie i przeczytanie pliku 'myfile.txt', a następnie zapisanie jego zawartosci w liscie
a = [int(x) for x in f.read().split()]

b= a[0]**a[1]+a[2] # Urzycie zawartości listy do rozwiązania równania

print('twoj wynik to:', b) # Wydrukowanie wyniku równania