import csv

archivoEntrada = open('rawT.csv')
entrada = csv.reader(archivoEntrada, delimiter=";")
archivoSalida=open("diff.csv","w")
salida=csv.writer(archivoSalida, delimiter=';')

diff = []


for row in entrada:

    if (row[0] == 'Dates'): #la fila de titulos
        diff.insert(0, [])
        i = 0 #i para recorrer la primera fila
        for title in row:
            diff[0].insert(i, (title + '_Inc'))
            i = i + 1
    else: #las filas de los datos
        fila = 1 #fila para saber en qué fila insertas el inc
        n = len(diff[0])
        j = 0 #j para recorrer las filas de datos
        for dato in row:
            diff.insert(i, [])
            if (j > 1 and j < (n - 2)):
                diff[fila].insert(j, float(dato.replace(',', '.')) - float(row[j].replace(',', '.')))
                #En la fila por la que vas guuardas en la posición j la dif entre el dato que hay ahí
                #y el que hay en la siguiente fila (el del día siguiente)
            j = j + 1 #paso de dato
        fila = fila + 1 #paso de fila

for row in diff:
    print(row)
archivoEntrada.close()
archivoSalida.close()
