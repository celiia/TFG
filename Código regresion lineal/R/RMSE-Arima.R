##para una serie de datos con periodo de un dia , que se tiene la informacion de 10 años.
 #En un principio se entrenaran los datos con  cinco años y se intentara predecir el dia sigyuiemte
 #En la siguiente iteracion se aumentara el conjunto de entrenamiento a cinco años y 7 dias y dedecira el dia siguiente
 #Y así hasta terminar con el conjunto de datos de 10 años
 # Los datos actuales y los predichos se guardaran en unos vectores los cuales luego se usaran para calcular el rmse
 
install.packages("Metrics")
library(openxlsx)
library(forecast)
library(Metrics)

col<-raw$EUR_Curncy_Open
dias_pred<-1
pred<-c()
act<-c()
start<-length(col)%/%2
avance<-seq(0,start-1,7)
for(i in avance){
  entrenamiento<-col[1:start+i]
  model<-arima(ts(entrenamiento),order=c(7,1,7),method="CSS")
  pred<-c(pred,c(forecast(model,dias_pred)$mean[1]))
  act<-c(act,c(col[start+i+dias_pred]))
  } 
rmse(act,pred)