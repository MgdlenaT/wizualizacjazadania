#Lab2.Z7
# Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. 
# Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.

lista = [1, 2.0, 3, 4.5, 8, 9.3] # tworzenie listy z liczbami typu int i float
list = []       # pusta lista, do której będziemy dodawać nowo utworzone liczby

for x in lista[::1]:
    x = x**2            # Podnoszenie do kwadratu każdej liczby z pierwszej listy i dodawanie jej do nowej listy
    list.append(x)

for x in list[::1]:     # Wydrukowywanie nowo utworzonej listy 
    print(x)

