# 1. Recorro la tabla para encontrar minsimo y maxsimo de cada columna (usando una lista de maxs y una de mins)
# 2. Recorro la tabla para escribir en el nuevo csv el dato escalado

import csv
import sys
archivoEntrada = open(sys.argv[1])
entrada = csv.reader(archivoEntrada, delimiter=";")
archivoSalida=open(sys.argv[2],"w")
salida=csv.writer(archivoSalida, delimiter=',')

# 1
maxs = []
mins = []
i = 0 # Fila
for row in entrada:
    j = 0 # Columna
    if (i != 0): # La primera fila no interesa
        for dato in row:
            if (j > 1): #Date y Date_Pretty no
                if (i == 1): # Guardo inicialmente el valor de la primera fila
                    maxs.append(float(dato))
                    mins.append(float(dato))
                else: # Recorro y actualizo maxs y mins
                    if (maxs[j-2] < float(dato)):
                        maxs[j-2] = float(dato)
                    if (mins[j-2] > float(dato)):
                        mins[j-2] = float(dato)
            j = j + 1
    i = i + 1

escalado = []
# 2
archivoEntrada.seek(0) #Volver al comienzo del csv
i = 0 # Fila
for row in entrada:
    j = 0 # Columna
    escalado.append([])
    for dato in row:
        if (i == 0): # Fila de titulos
            escalado[i].append(dato)
        else:
            if (j < 2): #Date y Date_Pretty
                escalado[i].append(dato)
            else:
                valor = float (dato)
                minc =  float (mins[j-2])
                maxc =  float (maxs[j-2])
                escalado[i].append(((valor - minc)/(maxc - minc))) # j - 2 por las dos primeras cols
        j = j + 1
    i = i + 1

for row in escalado:
    salida.writerow(row)

archivoEntrada.close()
archivoSalida.close()
