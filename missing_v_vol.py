import csv
import sys
archivoEntrada = open(sys.argv[1])
entrada = csv.reader(archivoEntrada, delimiter=",")
archivoSalida=open('volT.csv',"w")
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
            if (dato.startswith("US0003M") or dato.startswith("US0006M") or dato.startswith("US0012M") or dato.startswith("EUR") or dato.startswith("JPY") or dato.startswith("GBP") or dato.startswith("CHF")or dato.startswith("CAD")or dato.startswith("NOK")or dato.startswith("CNY")or dato.startswith("GSPG2YR")or dato.startswith("GSPG5YR")or dato.startswith("GSPG10YR")or dato.startswith("XAU")or dato.startswith("XAG")or dato.startswith("BDIY")or dato.startswith("CRY")):
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
