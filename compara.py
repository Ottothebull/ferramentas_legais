import csv
from time import sleep as sleep
import os
import tkFileDialog



file=raw_input("Endereco do primeiro arquivo:")

file2=raw_input("Endereco do segundo arquivo:")

lista1=[]
lista2=[]
iguais=[]
diferentes1=[]
diferentes2=[]
saida_iguais=[]
saida_diferentes1=[]
saida_diferentes2=[]
with open(file) as csv_file1:

    lido= csv.reader(csv_file1, delimiter=',')
    contador=0
    for row in csv_file1:
        contador=contador+1
        #print(row)
        lista1.append(row)

with open(file2) as csv_file2:

    lido2= csv.reader(csv_file2, delimiter=',')
    contador2=0
    for row in csv_file2:
        contador2=contador2+1
        lista2.append(row)
        
if contador>contador2 :
    for item1 in lista1:
        for item2 in lista2:
            if item1==item2:
                iguais.append(item1)
            
            else:
                sleep(0.1)
    for i in lista1:
        if i not in iguais:
            diferentes1.append(i)
    for i in lista2:
        if i not in iguais:
            diferentes2.append(i)

else :
    for item1 in lista2:
        for item2 in lista1:
            if item1==item2:
                iguais.append(item1)
            
            else:
                sleep(0.1)
    for i in lista1:
        if i not in iguais:
            diferentes1.append(i)
    for i in lista2:
        if i not in iguais:
            diferentes2.append(i)

##if contador > contador2:
##    intersec=set(lido).intersetion(lido2)

##else:
##    intersec=set(lido2).intersetion(lido)

##print(intersec)
for i in iguais:
    saida_=i.strip('\n')
    saida_iguais.append(saida_)

for i in diferentes1:
    saida_=i.strip('\n')
    saida_diferentes1.append(saida_)

for i in diferentes2:
    saida_=i.strip('\n')
    saida_diferentes2.append(saida_)


print("Presentes na Lista 1 e 2:")
print(saida_iguais)
print("Presentes apenas na Lista 1:")
print(saida_diferentes1)
print("Presentes apenas na Lista 2:")
print(saida_diferentes2)
csv_file1.close()
csv_file2.close()

os.system('PAUSE')