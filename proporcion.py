#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv
import numpy as np

archivoEntrada = open('trozoT.csv')
entrada = csv.reader(archivoEntrada, delimiter=";")
archivoSalida=open("difftrozo.csv","w")
salida=csv.writer(archivoSalida, delimiter=';')

diff = []
fila = 0

a = np.array(entrada)

for row in entrada:
    columna =0 # columna que voy rellenando en  la tabla
    
    if (row[0] == 'Dates'): #la fila de titulos
        diff.insert(fila, [])
       
        for title in row:
            diff[fila].insert(columna, (title + '_Inc'))
            columna = columna +1
        fila = fila + 1
     #else: #las filas de los datos
      #  fila = 1 #fila para saber en qué fila insertas el inc
       # n = len(diff[0])
       # j = 0 #j para recorrer las filas de datos
       # for dato in row:
        #    diff.insert(i, [])
        #    if (j > 1 and j < (n - 2)):
         #       diff[fila].insert(j, float(dato.replace(',', '.')) - float(row[j].replace(',', '.')))
                #En la fila por la que vas guuardas en la posición j la dif entre el dato que hay ahí
                #y el que hay en la siguiente fila (el del día siguiente)
          #  j = j + 1 #paso de dato
        #fila = fila + 1 #paso de fila
        
    else:
        for dato in row:
            if (dato == row[0]):
                diff.insert(fila, [])
                diff[fila].insert(columna,row[columna]) #la columna date se deja igual
                columna = columna+1
            elif(dato ==row[1]):
                diff[fila].insert(columna,row[columna])# la colunma date_pretty se deja igual
                # para los demas elementos que hay que hacer la proporcion
                columna=columna+1
            else:
       
                actual=(float(row[columna].replace(',', '.')))
                siguiente=1.5769 #float(().replace(',', '.'))# el elemento que esta en la misma columna pero en la fila(row)de abajo
                dif=abs(actual-siguiente)
        
                final = (dif/1)*(actual)
                diff[fila].insert(columna,str(final))
                columna= columna+1
        

for row in diff:
    print(row)
archivoEntrada.close()
archivoSalida.close()


# In[ ]:




