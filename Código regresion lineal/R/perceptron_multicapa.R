library(neuralnet)
futuros<-seq(2,50)
#probar para de dos a 50 futuros tarda mucho// intentarlo con  2(dia siguiente),10,15,30,40,50
for(h in futuros){

#sombres de todas las columnas open// de momento solo se usan las open
names<-c()
i<-seq(1,215,5) 
label<-1 
for(j in i){names<-c(names,colnames(raw[j]))}

#label es la columna a predecir, que se "sube" los dias que  se quiera predecir (h)
label<-scale(raw$EUR_Curncy_Open[h:nrow(raw)])
 
#en el dataframe data estará por cada fila,supuesto de que h =2 (predecir a un dia) : (valor euro de mañana), (valor euro hoy), (valor Jpy hoy),(valor NOk hoy).......
data<-data.frame(label)
for (j in i){col<-scale(raw[1:(nrow(raw)-(h-1)),j])
data<-data.frame(data,col)
}
#poner el nombre a las columnas
names(data) <- c("label",names)

#ignonar, era para probar con diferente umbrales
#data1rmse<-c()
data2rmse<-c()
#data3rmse<-c()
#data4rmse<-c()
#data5rmse<-c()
#data6rmse<-c()


train<-data[1:1315,]
ann <- neuralnet(label ~ EUR_Curncy_Open+JPY_Curncy_Open+GBP_Curncy_Open+CHF_Curncy_Open , train, hidden = 10, rep = 3,stepmax=1e6,threshold=0.05)

test<-data[1315:1415,]
output <- compute(ann, test[ , names [1:2]], rep = 1)

error<-rmse(test$label,output$net.result)
data2rmse<-c(data2rmse,error)


}

#para probar con diferetes umrales
#if(w==umbral[1]){data1rmse<-c(data1rmse,error)}
#else if(w==umbral[2]){data2rmse<-c(data2rmse,error)}
#else if(w==umbral[3]){data3rmse<-c(data3rmse,error)}
#else if(w==umbral[4]){data4rmse<-c(data4rmse,error)}
#else if(w==umbral[5]){data5rmse<-c(data5rmse,error)}
#else {data6rmse<-c(data6rmse,error)}

 