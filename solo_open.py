import csv
import sys
archivoEntrada = open(sys.argv[1])
entrada = csv.reader(archivoEntrada, delimiter=",")
archivoSalida=open(sys.argv[2],"w")
salida=csv.writer(archivoSalida, delimiter=',')

solo_open = []
col_open = 0
first = True
j = 0 #Fila
for row in entrada:
    i = 0 #Columna
    solo_open.append([])
    for dato in row:
        if (j == 0):
		if ("Open" in dato):
			if (first):
				col_open = i
				first = False
			solo_open[j].append(dato)
		elif(i == 0 or i == 1):
			solo_open[j].append(dato)
	else:
		print(col_open)
		if(col_open == (i%5) or i == 0 or i == 1):
           		solo_open[j].append(dato)
        i = i + 1
    j = j + 1
for row in solo_open:
    salida.writerow(row)

archivoEntrada.close()
archivoSalida.close()
