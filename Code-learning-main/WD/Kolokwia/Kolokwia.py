#Kolokwia
#1. (2pkt.) Napisz skrypt, który policzy
# i wyświetli następujące wyrażenie:

# import math
# wynik1= print(26**1/2)
# wynik2= print((math.sin(48))**2)
# wynik3= print(((26**1/2)+(math.sin(48))**2)**1/4)
# wynikzaokroglany=print(round(3.3975538061613855,2))

#2Napisz funkcje, która jako argument
# przyjmuje listę z liczbami. Zadaniem funkcji
# jest policzenie i wyświetlenie średniej wartości z elementów z
# listy, oraz liczbę elementów większych od średniej.
'''
def srednia(lista):
    return sum(lista)/len(lista)
lista = [1, 21, 3, 40]
average = srednia(lista)
print('Srednia elementow listy',average)
'''

#(5pkt.) Napisz skrypt, w którym utworzysz listę z liczbami.
# Zadaniem jest sprawdzenie czy na parzystych indeksach z listy są liczby większe od 0, wyświetl te liczby.
''' 
lista1=[2,3,6,5,1,-1,-8,12,-15] #stworzona lista
parzyste= lista1[0::2]  #parzyste indeksy z listy
print(parzyste)
for i in parzyste:
    if i>0:
        print(i) #liczby wieksze od zera
    '''


#Napisz skrypt, w którym utworzysz listę z liczbami dowolnego typu oraz wczytasz liczbę a.
# Zadaniem jest utworzenie nowej listy, gdzie elementy będą sumą poszczególnych elementów z pierwszej listy oraz liczby a.
# W programie dokonaj sprawdzenia błędów związanych z wczytywaną wartością, do tego celu użyj składni try-except.

lista2= [2,3,5,10]
while True:
    try:
        a= float(input("podaj liczbę a: "))
        suma = [i + a for i in lista2]
        print(suma)
        # sum=[i+i for i in suma]
        # print(sum)


    except ValueError:
        print("To nie byla liczba, spróbuj jeszcze raz")





