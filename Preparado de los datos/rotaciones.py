import csv
import sys
files = ['close', 'open', 'volat', 'volum']
for file in files:
    archivoEntrada = open(file+'_fc.csv')
    entrada = csv.reader(archivoEntrada,delimiter=",")

    archivosSalida = []
    results = []
    i = 0
    for lista in entrada: # Cada fila es una lista
        if (i != 0): #La primera no porque son las cabeceras
            results.append(lista)
        else:
            headers = lista
        i+=1

    tam = len(headers)

    for columna_predecir in range(0, tam):
        for futuro_a_predecir in range(1,91): #range(1,91)
            for pasado_a_utilizar in range(2,90): #range(2,90)
                fila =0 #fila que voy metiendo en el nuevo
                dia_actual=0 #dia por el que voy del viejo
                final=[]
                for row in results:
                    if(dia_actual>=futuro_a_predecir+pasado_a_utilizar-1):#empieza a partir de la fila 11
                        final.append([])
                        col = 0
                        for dato in row:
                            if col==columna_predecir:
                                dia=dato
                                pasado=results[dia_actual-futuro_a_predecir][col]
                                final[fila].append(float(dia)-float(pasado))
                            else:
                				final[fila].append(float(results[dia_actual-futuro_a_predecir][col])-float(results[dia_actual-futuro_a_predecir-pasado_a_utilizar+1][col]))
                            col+=1
                        fila+=1
                    dia_actual+=1
                name = file + '_c'+ str(columna_predecir)+'_'+str(futuro_a_predecir)+'_'+str(pasado_a_utilizar)
                archivoSalida=open(name+'.csv',"w")
                salida=csv.writer(archivoSalida,lineterminator='\n', delimiter=',')
                salida.writerow(headers)
                for fila in final:
                    salida.writerow(fila)
                archivoSalida.close()

    archivoEntrada.close()
