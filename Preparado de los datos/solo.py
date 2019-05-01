import csv
import sys
fichero=sys.argv[1]
ss=fichero.split('.')
archivoEntrada = open(fichero)
entrada = csv.reader(archivoEntrada, delimiter=",")
archivoSalidaOpen=open(ss[0]+'_open.csv',"w")
archivoSalidaClose=open(ss[0]+'_close.csv',"w")
archivoSalidaVolat=open(ss[0]+'_volat.csv',"w")
salidaOpen=csv.writer(archivoSalidaOpen, delimiter=',',lineterminator='\n')
salidaClose=csv.writer(archivoSalidaClose, delimiter=',',lineterminator='\n')
salidaVolat=csv.writer(archivoSalidaVolat, delimiter=',',lineterminator='\n')
solo_open = []
solo_close =[]
solo_volat = []
variables = [0,1,4]
col_names = ["Open", "Clos", "Volat"]
i = 0 #Fila
for row in entrada:
    j = -2 #Columna
    solo_open.append([])
    solo_close.append([])
    solo_volat.append([])
    for dato in row:
        if (i == 0): #Cabeceras
            if (col_names[0] in dato):
                solo_open[i].append(dato)
            elif(col_names[1] in dato):
                solo_close[i].append(dato)
            elif(col_names[2] in dato):
                solo_volat[i].append(dato)
            elif(j < 0): #Cabecera de fechas
                solo_open[i].append(dato)
                solo_close[i].append(dato)
                solo_volat[i].append(dato)
        else:
            if (j < 0): #Columnas de fechas
                solo_open[i].append(dato)
                solo_close[i].append(dato)
                solo_volat[i].append(dato)
            else: #Datos
                if (j%5 == variables[0]): #Open
                    solo_open[i].append(dato)
                elif (j%5 == variables[1]): #Close
                    solo_close[i].append(dato)
                elif (j%5 == variables[2]): #Volat
                    solo_volat[i].append(dato)
        j += 1
    i+=1

for row in solo_open:
    salidaOpen.writerow(row)
for row in solo_close:
    salidaClose.writerow(row)
for row in solo_volat:
    salidaVolat.writerow(row)

archivoSalidaClose.close()
archivoSalidaOpen.close()
archivoSalidaVolat.close()
archivoEntrada.close()
