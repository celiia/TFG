import csv
import sys
archivoEntrada = open(sys.argv[1])
entrada = csv.reader(archivoEntrada, delimiter=",")
archivoSalida=open(sys.argv[2],"w")
salida=csv.writer(archivoSalida, delimiter=',')

solo_open = []
j = 0 #Fila
for row in entrada:
    i = 0 #Columna
    solo_open.append([])
    for dato in row:
        if (i == 0 or i == 1 or ((i+2) % 4 == 0)): #Es la columna open (+2 por date y date_pretty)
            solo_open[j].append(dato)
        i = i + 1
    j = j + 1
for row in solo_open:
    salida.writerow(row)

archivoEntrada.close()
archivoSalida.close()
