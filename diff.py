#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv

archivoEntrada = open('rawT.csv')
entrada = csv.reader(archivoEntrada, delimiter=",")
archivoSalida=open("diff.csv","w")
salida=csv.writer(archivoSalida, delimiter=',')

diff = []
j = 0 #j es la fila
for row in entrada:
    if (j == 0): # Primera fila
        diff.append([])
        i = 0
        for title in row:
            if (row[i] == 'Dates' or row[i] == 'Date_pretty'):
                diff[j].append(title)
            else:
                diff[j].append(title + '_Inc')
            i = i + 1
    elif (j > 1): #El resto de filas (menos la 1, que no tiene anterior)
        diff.append([])
        i = 0 # i es la columna
        for dato in row:
            if (i == 0 or i == 1): #Dates y Date_Pretty
                diff[j-1].append(dato) #Es j-1 porque la 1 no se mete

            else: #Los valores
                if(float(dato)!=0):
                    diferencia = (abs(float(dato)-float(rowant[i])))
                    total = diferencia/(float(dato))
                    diff[j-1].append(total)
                else:
                    diff[j-1].append(0)

            i = i + 1
    rowant = row

    j = j + 1

for row in diff:
    salida.writerow(row)

archivoEntrada.close()
archivoSalida.close()


# In[ ]:
