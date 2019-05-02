library(Metrics)
prefix = 'C:/rafa/docencia/1819/tfg/keycapital/workflow'
setwd(prefix)
d <- read.csv("rawTV.csv")

d[1:2] <- list(NULL) 
normalize <- function(x)
{
    return((x- min(x)) /(max(x)-min(x)))
}
pega <- function(..., sep='') {
    paste(..., sep=sep, collapse=sep)
}
# escalado min-max
#d<-as.data.frame(lapply(d, normalize))+1

path = pega(prefix,'/data20_10_scaled_inc.txt')
f <- 100
p <- 200
max_col <- 15
cat("p: ",p," f: ",f,"\n",file = path, append = FALSE)

### nombres de las columnas de prediccion


for (col in seq(1,length(colnames(d)))) {
    present <- d[(p+2):(nrow(d)-f+1),col]

    future <- d[(f+p+1):nrow(d),col]
    # la etiqueta es el % de incremento en f días (saltando los p+1 primeros)
    label <- (future-present)/present
    
    rmse <- rmse(unlist(rep(0, length(label)), use.names=FALSE),unlist(label, use.names=FALSE))
    cat(colnames(d)[col],rmse,"\n",sep="",file = path, append = TRUE)

    rmse_up_to_now <- 1
    
    columns <- NULL
    column_names <- c()
    n <- 0
    puntoFijo <- FALSE # se pone a TRUE si una iteración no mejora
    cat("              ******   ",colnames(d)[col]," *******\n")
    cambios  <- 0
    while (n<max_col && !puntoFijo) {
        cat(" n=",n," ---")
    
        ndf <- columns
        ini <- 1
        fin <-  length(colnames(d)) 
        #ini <- 155
        #fin <- 165        
        for (i in seq(ini,fin)) {           
            nombres <- pega(colnames(d)[i],1)
            #cat(nombres,column_names)
            if (!(pega(colnames(d)[i],1) %in% column_names)) {
                pred<- i

                s <- seq(1,nrow(d))
                vs <- seq(0,p-1)

                name = colnames(d)[pred]
                names = c()
                for (v in vs) {
                  names = c(pega(name,(p-v)),names)
                }
                ## columnas para la prediccion
                df <- setNames(data.frame(matrix(ncol = p, nrow = 0)), names)
                for (row in seq(2,nrow(d)-p-f+1)) {
                    nrow = c()
                    for (v in vs) {
                      if (d[row-1+v,pred]){
                          nrow = c(nrow,(d[row+v,pred]-d[row+v-1,pred])/d[row-1+v,pred])
                      }else {
                          nrow = c(nrow,1)
                          }
                      #print(nrow)
                    }
                    df<-rbind(df, nrow)
                }
                names(df)<-names
                if (!is.null(columns)) {
                    df <- cbind(columns,df)
                }
                datos <- cbind(label,df)

                ######################
                ################# evaluación
                trainsize = 1500
                s = seq(trainsize,nrow(datos)-p-2)
                predichos <- c()
                reales <- c()
                #mirmse <- 0
                #m <- 0
                #vrmse <- c()
                for (j in s) {
                 train <- datos[1:j,]
                 rl <- lm(label ~ ., data = train)
                 coef<-rl$coefficients
                 test = datos[j+f+1,]
                 pred = coef[1]
                 for (x in seq(2,p+1)) {
                    pred = pred+test[x]*coef[x]
                 }
                 real = test[1]
                 #print(real)
                 #print(pred)
                 predichos <- c(predichos,pred)
                 reales <- c(reales,real)
                 #mirmse <- mirmse +((pred-real)*(pred-real))
                 #m <- m+1
                 #vrmse  <- c(vrmse,sqrt(mirmse/n))
                } 

                rmse <- rmse(unlist(reales, use.names=FALSE),unlist(predichos, use.names=FALSE))
                #cat("·",name,rmse,rmse_up_to_now,"\n")
                cambios <- cambios +1
                # un nuevo error mínimo?
                if (!is.na(rmse) & rmse<rmse_up_to_now) {
                   rmse_up_to_now <- rmse 
                   ndf  <- df
                   cat("nuevo max",name,rmse_up_to_now,"\n")
                   #cat(colnames(ndf),"\n",coef,"\n",file = path, append = TRUE)
                }
                #mirmse <- sqrt(mirmse/n)
            } #if
        }
        # cambiando columns
        if (cambios>0 || is.null(columns) || colnames(columns)!= colnames(ndf)) {
            columns <- ndf
            column_names <- colnames(columns)
            cat("            ******** CAMBIANDO COLUMNAS   ****",column_names,rmse_up_to_now,"\n")
            n <- n+1
            cat("Nueva columna",colnames(columns),rmse_up_to_now,"\n")
            #cat(colnames(columns),rmse_up_to_now,"\n",file = path, append = TRUE)
        } else {
          cat("Vuelta ",n," sin cambios \n")
          puntoFijo = TRUE
        }        
    } #while
    cat("==============  Acabado ==============", rmse_up_to_now,"\n\n") 
    cat(colnames(columns),rmse_up_to_now,"\n",file = path, append = TRUE)

}
