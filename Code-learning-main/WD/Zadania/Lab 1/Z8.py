# Lab1.Z8
# Zad.8 Zmienne łańcuchowe możemy dzielić. 
# Wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na poszczególne wyrazy. 
# (trzeba użyć metody split)

# treść piosenki jako zmienna
a = 'la la la la la la la la la la la la la la Teraz śpiewaj z nami la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la'

# dzielenie zmiennej i zapisywanie jej jako nowa zmienna
b = a.split()

# wydrukowanie nowoutworzonej zmiennej 
for x in b[::1]:
    print(x)