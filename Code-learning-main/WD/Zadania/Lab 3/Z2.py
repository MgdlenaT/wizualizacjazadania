#zadanie2
import random
randomlist=[]
#generowanie losowych 10 liczb z przedziału od 1 do 100
for i in range (10):
    n=random.randint(1,100)
    randomlist.append(n)
#wczytanie listy randomowych liczb
    print(randomlist)
#dodanie nowej listy python comprehension, która posiada tylko parzyste liczby z wygenerowanych
nowalista= [x for x in randomlist if x%2==0]
print(nowalista)