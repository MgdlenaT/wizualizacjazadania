#Zadanie4
#funkcja sprawdzajaca czy trojkat jest prostokątny
def trojkat_prostokatny(a,b,c):
    if a**2+b**2==c**2:
        return 'prostokatny'
    else:
        return 'nie jest prostokatny'
print(trojkat_prostokatny(5,4,5))