import csv

archivoEntrada = open('rawT_mv.csv')
entrada = csv.reader(archivoEntrada, delimiter=",")
archivoSalida=open("rawT.csv","w")
salida=csv.writer(archivoSalida, delimiter=',')

i = 0 #Fila
rawt = []
no_vale = [] # Tiene las posiciones de las columnas que no valen
for row in entrada:
    no_vale.append([])
    rawt.append([])
    j = 0 #Columna
    if (i == 0): #La fila de los titulos
        for dato in row:
            if (dato.startswith("EUR003M") or dato.startswith("EUR006M") or dato.startswith("EUR012M") or dato.startswith("CB3_Govt") or dato.startswith("CB6_Govt") or dato.startswith("CB12_Govt") or dato.startswith("ECCPEMUY")):
                no_vale.append(j) #Guardo las posiciones de las columnas que hay que borrar en cada fila
            else: #Si no es uno de esos, lo escribo                
                rawt[0].append(dato)
            j = j + 1
    else: #El resto de filas
        for dato in row:
            if (j not in no_vale): #Esa pos no es de una columna eliminada
                rawt[i].append(dato)
            j = j + 1
    i = i + 1
for row in rawt:
    salida.writerow(row)

archivoEntrada.close()
archivoSalida.close()