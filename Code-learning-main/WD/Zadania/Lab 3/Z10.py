
import random
randomlist=[]
#generowanie losowych 100 liczb z przedziału od 1 do 100
for i in range (101):
    n=random.randint(1,100)
    randomlist.append(n)
#dodanie nowej listy, która posiada tylko podzielne przez 4 liczby z wygenerowanych
nowalista= [x for x in randomlist if x%4==0]
print(nowalista)
f = open("liczby.txt", "w")