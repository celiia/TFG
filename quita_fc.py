# quitar las dos  primeras columnas y lass cabecera para procesar

import csv
import sys
fichero=sys.argv[1]
archivoEntrada = open(fichero)
entrada = csv.reader(archivoEntrada, delimiter=",")
ss=fichero.split('.')
archivoSalida=open(ss[0]+'_fc.csv',"w")
salida=csv.writer(archivoSalida, delimiter=',',lineterminator='\n')

nw=[]

rown =0
for row in entrada:

	row.pop(0)
	row.pop(0)
	
	nw.append(row)
	# borro las columnas de date y date_pretty
	rown+=1

		
for row in nw:
	
    salida.writerow(row)

archivoEntrada.close()
archivoSalida.close()
