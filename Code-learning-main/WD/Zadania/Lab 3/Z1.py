# Zadanie 1
#1-x dla x w przedziale od 1 do 10
A= [1-x for x in range(1,11)]
print(A)
#4 do potęgu i gdzie i jest w przedziale 1-7
B=[4**i for i in range(8)]
print(B)
#x z B jeśli jest liczbą parzystą
C=[x for x in B if  x%2==0]
print(C)