#funkcja wykorzystująca symbol **
#lista zakupów klucz- nazwa produktu, wartosc- koszt
#ile jest wszystkich produktów?
#całkowity koszt prdouktów
def lista_zakupow(** produkty):
    koszt_zakupow = 0
    for koszt in produkty:
        koszt_zakupow+=produkty[koszt]
    return len(produkty), round(koszt_zakupow,2)
print(lista_zakupow(mleko=2.78, ciastka=3.20, chleb=3.40, sok=5.70))