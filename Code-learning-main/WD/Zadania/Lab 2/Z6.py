# Lab2.Z6
# Wczytaj trzy liczby całkowite a,b,c i sprawdź,
# która z nich jest największa. 
# W zależności od wyniku wyświetl odpowiedni komunikat. 
# Użyj zagnieżdżeń.

i = input('Podaj 3 liczby calkowite, oddzielajac je spacja: ') # Pobieranie trzech liczb

a = [int(x) for x in i.split()] #tworzenie listy z podanych liczb

b = max(a) # sprawdzanie, która liczba jest największa

print('Liczba:', b, 'jest najwieszka!') # Zwracanie największej liczby