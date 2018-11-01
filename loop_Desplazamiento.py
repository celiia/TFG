#para fichero con open,volatilidad,volumen
#para la columna c
#dado un desplazamiento d[i],,i=[0,15,30,60,90,120,150,300]
#desplaza c d[i] dias
# y se intenta predecir c apartir del resto de columnas

#cargar un fihero solo con las columnas sin cabeceras
#y habiendole aplicado diff

import csv



archivoEntrada = open('prueba.csv')
entrada = csv.reader(archivoEntrada, delimiter=";")
archivoSalida=open("uno.csv","w")
salida=csv.writer(archivoSalida, delimiter=',')

c=0
d=[0,15,30,60]
contadorReal=0
contadorDesplazada=0
nueva=[]

for dato in d:#por cada desplazamirento
	print(dato)
	
	for dia in entrada:
		num=dia[c]
		dia[c]=''
		nueva.append(dia) # se meten sin los datos de la primera fila que se rellenaran mas tarde
		
		if(contadorReal >=float(dato)-1):
			
			nueva[contadorDesplazada][c]=num
			contadorDesplazada+=1
		contadorReal+=1
	
	contadorReal=0
	contadorDesplazada=0
	archivoEntrada.seek(0)
	nueva=[]
	
	
	for i in nueva:
		print(i)
	
	
	


archivoEntrada.close()
archivoSalida.close()
 
 
 

