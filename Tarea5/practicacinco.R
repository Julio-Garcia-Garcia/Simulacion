for(i in 1:10){
  desde <- 3
  hasta <- 7
  pedazo <- 500000
  target <- 0.0488341 #debemos de llegar a este número
  integral <- 0
  suma <- 0
  contador <- 0
  decimales <-2   #cantidad de decimales que debemos respetar
  
  f <- function(x) { return(1 / (exp(x) + exp(-x))) }
  g <- function(x) { return((2 / pi) * f(x)) }
  suppressMessages(library(distr))
  generador  <- r(AbscontDistribution(d = g)) # creamos un generador            
  parte <- function() {
    valores <- generador(pedazo)
    return(sum(valores >= desde & valores <= hasta))
  }
  
  while( abs((pi / 2) * integral - target) > 1*10^((-1)*decimales - 1)) {
    contador <- contador + 1
    montecarlo <- parte()
    suma <- suma + montecarlo
    integral <- suma / (contador * pedazo)
  }
  print(c(i,decimales,(pi / 2) * integral,contador))
}
