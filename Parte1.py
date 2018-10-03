#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
csvarchivo = open('trozo.csv',encoding="utf8",errors='ignore')
entrada = csv.reader(csvarchivo, delimiter=";")
archivoSalida=open("trozoT.csv","w",newline='')
salida=csv.writer(archivoSalida, delimiter=';')

traspuesto =[]# la columna por la que va creando la traspuesta
j=2
for row in entrada: # las filas de la tabla inicial
    i=0
    
    
    if (row[2]=='Dates'): #si la fila es la de fechas
        traspuesto.insert(i,['Dates','Date_pretty'])
        i=i+1
        for fecha in row:
            if(fecha.isdigit()): #por cada fecha valida
                traspuesto.insert(i,[fecha,'fecha_hacer']) #insertar en la posicin cero de la fila i
                i=i+1
     #si no es la fila de la fecha
    else:
        for dato in row: #en cada iteracion se rellenan para todas las monedas la informacion de un campo
            
            if(i==0):#en la fila 0 pongo el titulo de la columba correspondiente a j
                traspuesto[i].insert(j,(row[0].split()[0])+'_'+(row[0].split()[1])+'_'+(row[1].split()[0]))
                i=i+1
            else:   #cuando dato corresponde a la informacion del dia
                if((dato!=row[1]) and (dato !=row[2])): #si dato no es ni la columna dos ni tres que tienen string queno nos interesan
                    traspuesto[i].insert(j,dato) #inserto en la fila i(el dia) en la columna j  que este rellenando en esta iteracion
                    i=i+1 #aumento la  fila(dintinto dia)porque  row esta la info de varios dias
            
        
    j=j+1 # la siguente columna a rellenar
            
        
print (traspuesto)
        
        




# In[ ]:




