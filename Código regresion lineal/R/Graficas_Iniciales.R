raw <- read.csv("Desktop/TFG/rawTV.csv")
raw<-raw[,-1]
raw<-raw[,-1]

m=350 #El día a predecir
p = 6 #Con los datos de hace 3 días
h=10 #Predecir lo que pasa dentro de 10
euro <-raw$EUR_Curncy_Open
f <- fit <- Arima(ts(euro[1:(m-h)]), order=c(3,1,1))
autoplot(ts(euro[1:m])) +
  autolayer(forecast(f,h)) +
  autolayer(meanf(ts(euro[1:(m-h)]), h=h),
            series="Mean", PI=FALSE) +
  autolayer(naive(ts(euro[1:(m-h)]), h=h),
            series="Naïve", PI=FALSE) +
  autolayer(snaive(ts(euro[1:(m-h)]), h=h),
            series="Seasonal naïve", PI=FALSE) +     
  autolayer(ts(euro[1:m])) +
  ggtitle("Predicción euro") +
  xlab("Día") + ylab("Valor") +
  guides(colour=guide_legend(title="Predicción"))


  for (i in avance) {
euro2 <- scale(raw$EUR_Curncy_Open[(dias_pred+pasado):(start-pasado)+i]) # maÃ±ana start: hasta donde llega el conjunto de entrenamiento
nok1 <- scale(raw$EUR_Curncy_Open[1:((start-pasado)-3)]) # antes de ayer(n+1-1)
nok2 <- scale(raw$NOK_Curncy_Open[2:((start-pasado)-2)]) # ayer(n+1-2)
nok3 <- scale(raw$NOK_Curncy_Open[3:((start-pasado)-1)]) # hoy(n+1-3)
linearMod <- lm(euro2 ~ nok1)
linearMod2 <- lm(euro2 ~ nok1+nok2+nok3)
c <- linearMod2$coefficients

 # el -pasado es porque se predice el +4 y queremos que sea el mismo dia que en los metodos anteriones

ed = c[1]+c[2]*scale(raw$NOK_Curncy_Open[start+i+1])+c[3]*scale(raw$NOK_Curncy_Open[start+i+2])+c[4]*scale(raw$NOK_Curncy_Open[start+i+3])
pred5<-c(pred5,c(ed))

}
lmE<-rmse(act,pred5)
           