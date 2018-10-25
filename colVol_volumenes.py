import csv

archivoEntrada = open('rawT_volumenes.csv')
entrada = csv.reader(archivoEntrada, delimiter=",")
archivoSalida=open("rawTV_volumenes.csv","w")
salida=csv.writer(archivoSalida, delimiter=',')

rawtv= []
nrow=0
poshigh=2
poslow=3
k=-2
for row in entrada:


    rawtv.append([])
       #fila de nombres
    if(row[0]=='Dates'):

        for dato in row:


            if(dato.endswith("Low")):
                rawtv[nrow].append(dato)
                partes=dato.split("_")
                rawtv[nrow].append(partes[0]+'_'+partes[1]+'_Volatility')
            else:
                 rawtv[nrow].append(dato)
            k=k+1

       #filas de datos
    else:

        col=0
        high=0
        low=0
        vol=0

        for dato in row:


            if(col!=0 and col !=1):#guardo los valores e high y low

                if(vol==poshigh):
                    high=dato

                elif(vol==poslow):
                    low=dato

                vol=vol+1


            if(vol!=posvolum):# si es una columna distinta de volum (ultima) guardo el dato normal
                rawtv[nrow].append(dato)
            else:#melo low y volatility
                rawtv[nrow].append(dato)
                #print ("EOOOOOOOO    " + high + "     " + low )
                dd=float(high)-float(low)


                rawtv[nrow].append(dd)
                vol=0


            col=col+1
    nrow=nrow+1

for fila in rawtv:
    salida.writerow(fila)

archivoEntrada.close()
archivoSalida.close()
