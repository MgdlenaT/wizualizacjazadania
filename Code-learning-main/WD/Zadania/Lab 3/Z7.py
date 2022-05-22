def iloczyn_ciag(*liczby, b):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn_liczb = liczby[0] * b
        for a in range(1, len(liczby), 1):
            iloczyn_liczb *= b
        return iloczyn_liczb
print(iloczyn_ciag(1,2,3,4,5,6,7,8,9,10,b=4))