# sacar el RMSE con auto arima de todas las  columnas de datos antes escaladas para poder comparar


 c <- seq (1,215,5)
 new<-matrix(nrow=1,ncol=3)
 new[1,]<-c("Names","RmseEscalado","RmseSinEscalar")
 
 for(i in c) {fit<-auto.arima(scale(raw[,i]))
 	fit2<-auto.arima(raw[,i])
	new<-rbind(new,c(colnames(raw)[i],accuracy(fit)[2],accuracy(fit2)[2]))}
	write.table(new, "tablita.csv", sep=",", row.names = FALSE, col.names = FALSE)
 
 new <- read.csv("tablita.csv")
 new<-arrange(new, RmseEscalado)
 write.table(new, "tablita2.csv", sep=",", row.names = FALSE, col.names = TRUE)