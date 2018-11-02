import csv
import datetime
import sys
from datetime import date, timedelta

archivoEntrada = open(sys.argv[1])
entrada = csv.reader(archivoEntrada, delimiter=";")
archivoSalida=open(sys.argv[2],"w")
salida=csv.writer(archivoSalida, delimiter=',')

traspuesto =[]# la columna por la que va creando la traspuesta
j=2
for row in entrada: # las filas de la tabla inicial
    i=0
    if (row[2]=='Dates'): #si la fila es la de fechas
        traspuesto.insert(i,['Dates','Date_pretty'])
        i=i+1
        for fecha in row:
            if(fecha.isdigit()): #por cada fecha valida
                start = date(1900,1,1)

                delta = timedelta(int(fecha))

                offset =  start + delta

                traspuesto.insert(i,[fecha,offset.strftime('%d/%m/%Y')]) #insertar en la posicin cero de la fila i
                i=i+1
     #si no es la fila de la fecha
    else:
        for dato in row: #en cada iteracion se rellenan para todas las monedas la informacion de un campo
            dato = dato.replace(",", ".")
            if(i==0):#en la fila 0 pongo el titulo de la columba correspondiente a j
                traspuesto[i].insert(j,(row[0].split()[0])+'_'+(row[0].split()[1])+'_'+(row[1].split()[0]))
                i=i+1
            else:   #cuando dato corresponde a la informacion del dia
                if((dato!=row[1]) and (dato !=row[2])): #si dato no es ni la columna dos ni tres que tienen string queno nos interesan
                    traspuesto[i].insert(j,dato) #inserto en la fila i(el dia) en la columna j  que este rellenando en esta iteracion
                    i=i+1 #aumento la  fila(dintinto dia)porque  row esta la info de varios dias


    j=j+1 # la siguente columna a rellenar


for fila in traspuesto:
    salida.writerow(fila)

archivoEntrada.close()
archivoSalida.close()
