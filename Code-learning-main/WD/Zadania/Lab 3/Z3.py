#słownik z produktami spożywczymi
#klucz= nazwa produktu, wartość=jednostka
produkty={'chleb':'sztuki','mąka':'kg', 'mleko':'sztuki'}
print(produkty)
#python comprehension z produktami ktorych wartosc to sztuki
a=[key for key in produkty.keys() if produkty[key] == 'sztuki']
print(a)