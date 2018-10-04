import csv

archivoEntrada = open('rawT.csv')
entrada = csv.reader(archivoEntrada, delimiter=";")
archivoSalida=open("diff.csv","w")
salida=csv.writer(archivoSalida, delimiter=';')

diff = []

for row in entrada:

    if (row[0] == 'Dates'): #la fila de titulos
        diff.insert(0, [])
        i = 0
        for title in row:
            diff[0].insert(i, (title + '_Inc'))
            i = i + 1

for row in diff:
    print(row)
archivoEntrada.close()
archivoSalida.close()
