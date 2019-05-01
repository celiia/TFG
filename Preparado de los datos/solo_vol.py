import csv
import sys
fichero=sys.argv[1]
ss=fichero.split('.')
archivoEntrada = open(fichero)
entrada = csv.reader(archivoEntrada, delimiter=",")
archivoSalida=open('escalado_volum.csv',"w")
salida=csv.writer(archivoSalida, delimiter=',',lineterminator='\n')
solo_volum = []
col_volum = 4
i = 0 #Fila
for row in entrada:
    j = -2 #Columna
    solo_volum.append([])
    for dato in row:
        if (i == 0): #Cabecera
            if (j < 0): #Fechas
                solo_volum[i].append(dato)
            elif ("Volume" in dato): #Columna de volum
                solo_volum[i].append(dato)
        else:
            if ((col_volum == j%5) or j < 0):
           		solo_volum[i].append(dato)
        j+=1
    i+=1


for row in solo_volum:
    salida.writerow(row)
archivoEntrada.close()
archivoSalida.close()
