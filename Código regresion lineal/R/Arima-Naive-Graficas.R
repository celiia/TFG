





#crear una tabla y posterirmente un agrafica con los siguientes datos:
#Nombres de columnas: Valor de la bolsa, Avance en el tiempo,  Prediccion en el tiempo, Número de datos,Arima-SinEscalar,Arima-Escalado
#RegresionLineal-SinEscalar, RegresionLineal-Escalado, Naïve-SinEscalar, Naïve-Escalado, SeasonalNaïve-SinEscalar, SeasonalNaïve-Escalado
# hacerlo para 30 valores de euro

dias_pred<-10
valores<-raw$EUR_Curncy_Open
valoresEscalados<-scale(valores)
start<-length(valoresEscalados)%/%2
avance<-seq(0,2631,7)
pred<-c()
pred2<-c()
pred3<-c()
pred4<-c()
act<-c()
#ARIMA
for(i in avance){
  entrenamiento<-valoresEscalados[1:start+i]
  model<-Arima(ts(entrenamiento),order=c(7,1,7),method="CSS")
  pred<-c(pred,c(forecast(model,dias_pred)$mean[1]))
  act<-c(act,c(valoresEscalados[start+i+dias_pred]))
}
arimaSE<-rmse(act,pred)

#NAIVE
for (i in avance) {
  pred2<-c(pred2,c(naive(ts(valoresEscalados[1:start+i]), h=dias_pred)$mean[dias_pred]))
}
naiveSE<-rmse(act,pred2)

#SEASONAL NAIVE
for (i in avance){
  pred3<-c(pred3,c(snaive(ts(valoresEscalados[1:start+i]), h=dias_pred)$mean[dias_pred]))
}
naiveSeasonalSE<-rmse(act,pred3)

#MEAN
for (i in avance) {
  pred4<-c(pred4,c(meanf(ts(valoresEscalados[1:start+i]), h=dias_pred)$mean[dias_pred]))
}
meanfSE<-rmse(act,pred4)

#regresion lineal (de momento solo con el Euro consigo  mismo hace tres dias)
pred5<-c()
pasado<-3
#primero que predice es el cuarto
for (i in avance) {
euro2 <- raw$EUR_Curncy_Open[(dias_pred+pasado):(start-pasado)+i] # mañana start: hasta donde llega el conjunto de entrenamiento
nok1 <- raw$NOK_Curncy_Open[1:((start-pasado)-3)] # antes de ayer(n+1-1)
nok2 <- raw$NOK_Curncy_Open[2:((start-pasado)-2)] # ayer(n+1-2)
nok3 <- raw$NOK_Curncy_Open[3:((start-pasado)-1)] # hoy(n+1-3)
linearMod <- lm(euro2 ~ nok1)
linearMod2 <- lm(euro2 ~ nok1+nok2+nok3)
c <- linearMod2$coefficients

 # el -pasado es porque se predice el +4 y queremos que sea el mismo dia que en los metodos anteriones

ed = c[1]+c[2]*raw$NOK_Curncy_Open[start+i+1]+c[3]*raw$NOK_Curncy_Open[start+i+2]+c[4]*raw$NOK_Curncy_Open[start+i+3]
pred5<-c(pred5,c(ed))

}
lmSE<-rmse(act,pred5)
           

#data framed

n<-data.frame(arimaSE,naiveSE,naiveSeasonalSE,meanfSE,lmSE)
n


#hacer graficas
dia <- seq(1:14)
new1<-data.frame(dia,pred,act,pred2,pred3,pred4,pred5)
ggplot(new1) +
  geom_point(mapping = aes(x = dia, y = act,color = "Real") , size = 5)+
  geom_line(mapping = aes(x = dia, y = act,color = "Real"),  size = 2) +
  geom_line(mapping = aes(x = dia, y = pred2,color = "Naive"),  size = 1) +
  geom_line(mapping = aes(x = dia, y = pred3,color = "SeasonalNaive"), size = 1)+
  geom_line(mapping = aes(x = dia, y = pred4,color = "Mean"),  size = 1)+
  geom_line(mapping = aes(x = dia, y = pred ,color = "Arima"), size = 1)+
  geom_line(mapping = aes(x = dia, y = pred5 ,color = "R.lineal"), size = 1)+
  scale_color_manual(values=c("Real"="green","Naive"="pink","SeasonalNaive"="blue","Mean"="orange","Arima"="red","R.lineal"="purple"))







