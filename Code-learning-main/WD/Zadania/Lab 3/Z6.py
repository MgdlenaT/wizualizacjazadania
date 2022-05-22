#Funkcja licząca iloczyn elementów ciągu a-wartosc początkowa,
# b-wielokosc o ile mnozone sa kolejne elementy, ile-ile elementow ma mnozyc
def iloczyn_el_ciagu(a=1,b=4,ile=10):
    licznik=0
    while licznik != ile:
        a*=b
        licznik+=1
    return a
print(iloczyn_el_ciagu())


