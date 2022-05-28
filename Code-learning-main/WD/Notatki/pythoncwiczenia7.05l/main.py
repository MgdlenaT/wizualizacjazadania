#pandas 1.4.0
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
# a= np.arange(12).reshape((4,3))
# print(a)
# print(a.sum())
# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.sum(axis=1))
# b=np.array([20,30,40,50])
# c=np.arange(4)
# d=c+b
# print(d)
# e=np.sqrt(c)
# f=d+e
# print(f)
# a=np.array([[2,5,1],[3,7,1]])
# b=np.array([[2,3],[3,2],[7,1]])
# c=np.dot(a,b)
# print(c)
# #2sposobmnozenie
# d= a.dot(b)
# print(d)
#
# e=np.arange(3)
# f=np.arange(3)
# print(np.dot(e,f))
# g=np.arange(3)
# h=np.array([[0],[1],[2]])
# print(g.dot(h))
# a=np.arange(6).reshape((3,2))
# print(a.flat)
# # for b in a.flat:
# #     print(b) #splaszczyc maciez do jednowym tablicy i flat dostep do kazdego elementu oddzielnie
# c=a.reshape((2,3))
# print(c)
# b=c.ravel() #format wyjsciowy
# print(b)
# d=c.T #transpozycja zamiania  wierszy i kolumn
# print(d)
#Pandas
# s=pd.Series([1,3,4,'a',3.5])
# print(s)
# s=pd.Series([10,12,14,8], index=['a','b','c','d'])
# print(s)
# data= {'Kraj':['Belgia','Indie','Brazylia'],
#        'Stolica':['Bruksela','New Delhi','Brazylia'],
#        'Populacja':[12356743879, 467328567,12345637]}
# df=pd.DataFrame(data) #ramkadanych-slownik
# # print(df)
# # daty= pd.date_range('20220507',periods=5)
# # print(daty)
# # df2=pd.DataFrame(np.random.randn(5,4),index=daty,columns=list('ABCD'))
# # print(df2)
# df3=pd.read_csv('dane.csv',header=0,sep=';',decimal='.')
# print(df3)
# df3.to_csv('dane2.csv',index=False)
# xlsx=pd.ExcelFile('imiona.xlsx')
# df=pd.read_excel(xlsx,header=0)
# df.to_excel('imiona2.xlsx',sheet_name='dane')
# print(df)
#openpyxl
# print(s['a'])
# print(s.a)
# print(df[0:1])
# print(df['Kraj'])
# print(df.Kraj)
#
# print(df.iloc[[0],[0]])
# print(df.loc[[0],['Kraj']])
# print(df.at[0,'Kraj'])
# print(df.sample(2))
# print(df.sample(10,replace=True))
#print(df4.head(10))
#print(df4.tail(10))
# print(s['a'])
# print(s.a)
#
# print(df[0:1])
# print(df['Kraj'])
# print(df.Kraj)
#
# print(df.iloc[[0],[0]])
# print(df.loc[[0],['Kraj']])
# print(df.at[0,'Kraj'])
#
# print(s[s>8])
# print(s[(s<13)&(s>8)])
#
# print(s.where(s>10,'warunek niespełniony'))
# seria=s.copy()
# seria.where(s>10,'warunek niespełniony',inplace=True)
# print(df[df['Populacja'] > 12000000])
# s['s']=14
# print(s)
# df.loc[3] = 'nowy element'
# print(df)

# df.loc[4]= ['Polska','Warszawa',345678]
# print(df)
#
# df.drop([3],inplace=True)
# print(df)

# df['Kontynent']=['Europa','Azja','Ameryka Południowa','Europa']
# print(df)
#
# print(df.sort_values(by='Kraj'))
# new=df.sort_values(by='Kraj')
# print(new)

# grupa=df.groupby(by='Kontynent').agg({'Populacja':['sum']})
# print(grupa.get_group('Europa'))
# print(grupa.agg({'Populacja':['sum']}))
#matplotlib 3.5.1 wykres
# grupa.plot(kind='bar', xlabel='Kontynenty',ylabel='Populacja w mln',rot=0,title='Populacja na kontynentach')
# plt.savefih('plot1.png') #egz
# plt.show()

# wykres=grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Populacja w mln')
# wykres.tick_params(axis='s',labelrotation=0)
# wykres.set_title('Populacja na kontynentach')
# plt.savefig('plot1.png')/
# plt.show()
# grupa=df3.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# grupa=df3.groupby('Imię i nazwisko').agg({'Wartość zamówienia':['sum']})
# print(grupa)
# grupa.plot(kind='pie',subplots=True,autopct='%.2f %%',fontsize=20,colors=['red','green'])
# plt.legend(loc='upper left')
# plt.show()

# seria=pd.Series(np.random.randn(1000))
# seria=seria.cumsum()
#
# seria.plot()
# plt.show()

# plt.plot([1,2,3,4],[1,4,9,16],'ro:')
# plt.ylabel('Liczby z wektora')
# plt.show()
#
# plt.plot([1,2,3,4],[1,4,9,16],'r:')
# plt.plot([1,2,3,4],[1,4,9,16],'bo:')
#
# plt.axis([9,6,0,20])

# x=np.arange(0,5.2,0.2)
# # plt.plot(x,x,'r-',x,x**2,'b',x,x**2,'gs')
# # plt.legend(labels=['liniowa','kwadratowa','szescienna'],loc='central left')
# # plt.show()
# plt.plot(x,x,label='liniowa')
# plt.plot(x,x**2, label='kwadratowa')
# plt.plot(x,x**3,label='szescienna')
# plt.legend()
# plt.savefig('plot.png')
# plt.show()
# im1=Image.open('plot.png')
# im1=im1.convert('RGB')
# im1.save('plot.jpg')

# x=np.arange(1,21,1)
# plt.plot(x,1/x,'ro:',label='x/')
# plt.legend()
# plt.show()
#
#
# x1=np.arange(0,11,0.1)
# plt.plot(x1, np.sin(x1),'b-',label='x1')
# plt.legend()
# plt.show()

# x1=np.arange(0,2.02,0.02)
# x2=np.arange(0,2.02,0.02)
# y1=np.sin(2*np.pi*x1)
# y2=np.cos(2*np.pi*x1)
# plt.subplot(2,1,1)
# plt.plot(x1,y1,'r--')
# plt.ylabel('sin(y)')
#
# plt.subplot(2,1,2)
# plt.plot(x2,y2,'go')
# plt.xlabel('x')
# plt.ylabel('cos(y)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# fig,axs=plt.subplots(3,2)
#
# print(type(fig))
# print(type(axs))
#
# axs[0,0].plot(x1,y1,'r-')
# axs[0,0].set_xlabel('x')
# axs[0,0].set_ylabel('sin(x)')
# axs[0,0].set_title('wykres sin(x)')
#
# axs[1,1].plot(x2,y2,'g-')
# axs[1,1].set_xlabel('x')
# axs[1,1].set_ylabel('sin(x)')
# axs[1,1].set_title('wykres cos(x)')
#
# axs[2,0].plot(x2,y2,'g-')
# axs[2,0].set_xlabel('x')
# axs[2,0].set_ylabel('sin(x)')
# axs[2,0].set_title('wykres cos(x)')
# fig.delaxes(axs[0,1])
# fig.delaxes(axs[1,0])
# fig.delaxes(axs[2,1])
# plt.show()

# dane={'a':np.arange(50),
#       'c':np.random.randint(0,50,50),
#       'd':np.random.randn(50)}
# dane['b']=dane['a']+10*np.random.randn(50)
# dane['d']=np.abs(dane['d'])*100
#
# plt.scatter(data=dane,x='a',y='b',c='c',s='d')
# plt.xlabel('wartosci a')
# plt.ylabel('wartosci b')
# plt.show()
# print(dane['c'])

# dane={'Kraj':['Belgia','Indie','Brazylia','Polska'],
#         'Stolica':['Bruksela','New Delhi','Brasilia','Warszawa'],
#        'Populacja':[1235674387, 4673285679,2878563745,38675467],
#       'Kontynent':['Europa','Azja','Ameryka Południowa','Europa']}
# df=pd.DataFrame(dane)
# print(df)
# grupa=df.groupby('Kontynent')
# etykiety=list(grupa.groups.keys())
# wartosc=list(grupa.agg('Populacja').sum())
#
# plt.bar(x=etykiety,height=wartosc,color=['red','green','blue'])
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja na kontynentach')
# plt.show()

x=np.random.randn(10000)
plt.hist(x,bins=15,facecolor='g',alpha=0.75,density=True)
plt.xlabel('wartosci x')
plt.ylabel('prawdopodobienstwa')
plt.show()


