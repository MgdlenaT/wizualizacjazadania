import numpy as np #1.22.2
import matplotlib.pyplot as plt #3.5.1
import pandas as pd #1.4.0
import openpyxl #3.0.9

# Zadanie 1
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx

xlsx=pd.ExcelFile('datasets/imiona.xlsx')
df=pd.read_excel(xlsx,header=0)
print(df)
df.to_excel('imiona.xlsx',sheet_name='arkusz pierwszy')
#Zadanie 2
# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
# • tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# • tylko rekordy gdzie nadane imię jest takie jak Twoje
# • sumę wszystkich urodzonych dzieci w całym danym okresie,
# • sumę dzieci urodzonych w latach 2000-2005
# • sumę urodzonych chłopców i dziewczynek,
# • najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# • najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
'''print(df[df.Liczba>1000])
print(df[df.Imie=='MAGDALENA'])
print(df.Liczba.sum())
grupa=df[df.Rok>2006].groupby('Rok').agg({'Liczba':['sum']})
print(grupa)

grupa1 = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa1)
wykres = grupa1.plot.bar(ylabel='Liczba urodzeń')
wykres.legend()
plt.xticks(rotation=0)
plt.title("Liczba urodzonych chłopców i dziewczynek")
plt.show()
print('')
#• najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())

#• najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
for index, group in enumerate(new_df, start=1):
    print(f"{index} {group[0]}")
    print(f" {group[1].iloc[0]['Imie']}", end='')
    print(f" {group[1].iloc[0]['Liczba']}")
print('')
print("Chłopiec")
print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
                                                                                   ascending=False).iloc[0])
print("Dziewczynka")
print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),ascending=False).iloc[0])
'''
# Zadanie 3
# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:
# • listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z
# DataFrame)
# • 5 najwyższych wartości zamówień
# • ilość zamówień złożonych przez każdego sprzedawcę
# • sumę zamówień dla każdego kraju
# • sumę zamówień dla roku 2005, dla sprzedawców z Polski
# • średnią kwotę zamówienia w 2004 roku,
# • zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku
# zamówienia_2005.csv
df = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
print(df)
# • listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z
# DataFrame)
print(df.Sprzedawca.unique())
print('')
# • 5 najwyższych wartości zamówień
print(df.sort_values('Utarg', ascending=False).head(5))
print('')
#• ilość zamówień złożonych przez każdego sprzedawcę
print(df.groupby('Sprzedawca').size())
#sumę zamówień dla każdego kraju
print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
#sumę zamówień dla roku 2005, dla sprzedawców z Polski
print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].
      agg({'Utarg': ['sum']}))
print('')
# • średnią kwotę zamówienia w 2004 roku,
print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))

#zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku
# zamówienia_2005.csv
rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
rok_2004.to_csv("zamowienia_2004.csv", index=False)
rok_2005 = df[((df[ 'Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31'))]
rok_2005.to_csv("zamowienia_2005.csv", index=False)
