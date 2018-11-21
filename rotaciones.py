#!/usr/bin/env python
# coding: utf-8

# In[35]:


import csv
import sys
fichero = sys.argv[1]

archivoEntrada = open(fichero)
entrada = csv.reader(archivoEntrada,delimiter=",")

ss=fichero.split('.')
archivoSalida=open(ss[0]+'_rotado.csv',"w")
salida=csv.writer(archivoSalida,lineterminator='\n', delimiter=',')


results = []
for lista in entrada: # Cada fila es una lista
    results.append(lista)
        
futuro_a_predecir=11
pasado_a_utilizar=4

print(results)


columna_predecir=1

fila =0 #fila que voy metiendo en el nuevo
dia_actual=0 #dia por el que voy del viejo
final=[]
for row in results:
    if(dia_actual>=futuro_a_predecir+pasado_a_utilizar-1):#empieza apartir de la fila 11
        
        final.append([])
        col =0
        for dato in row:
            if col==0:
                final[fila].append(dia_actual)
            elif col==columna_predecir:
                
                dia=dato
                pasado=results[dia_actual-futuro_a_predecir][col]
               
                
                final[fila].append(float(dia)-float(pasado))
            else:
				final[fila].append(float(results[dia_actual-futuro_a_predecir][col])-float(results[dia_actual-futuro_a_predecir-pasado_a_utilizar+1][col]))
                
                
            col+=1
        
        
        fila+=1
    
    dia_actual+=1
    
for fila in final:
    salida.writerow(fila)

archivoEntrada.close()
archivoSalida.close()
    


# In[ ]:





# In[ ]:




