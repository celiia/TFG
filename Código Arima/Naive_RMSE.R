#library(Metrics)
raw <- read.csv("Desktop/TFG/rawTV.csv")
futuros <- c(1,7,15,30,60)
valores<-raw$NOK_Curncy_Open
valoresEscalados<-scale(valores)
start<-length(valoresEscalados)%/%2
tabla <- c()
tabla <- rbind(tabla, c("Periodo", "seasonalNaiveRMSE", "naiveRMSE"))

for (futuro in futuros){
  avance<-seq(0,188,7)
  act<-c()
  for(i in avance){
    entrenamiento<-valoresEscalados[1:start+i]
    act<-c(act,c(valoresEscalados[start+i+futuro]))
  }
  naive_pred<-c()
  snaive_pred<-c()
 
  #NAIVE
  for (j in avance) {
    naive_pred<-c(naive_pred,c(naive(ts(valoresEscalados[1:start+j]), h=futuro)$mean[futuro]))
  }
  naiveRMSE<-rmse(act,naive_pred)
  
  #SEASONAL NAIVE
  for (k in avance){
    snaive_pred<-c(snaive_pred,c(snaive(ts(valoresEscalados[1:start+k]), h=futuro)$mean[futuro]))
  }
  naiveSeasonalRMSE<-rmse(act,snaive_pred)
  
  tabla <- rbind(tabla, c(futuro, naiveSeasonalRMSE, naiveRMSE))
}

write.table(tabla, "Desktop/TFG/naive/Naive_NOK.csv", sep=",", row.names = FALSE, col.names = FALSE)
