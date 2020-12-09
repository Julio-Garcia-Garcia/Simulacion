CantAciertos <- read.csv("tdoce.csv")
CantAciertos
attach(CantAciertos)
names(CantAciertos)
str(CantAciertos)
FactorA_ProbNegro <- factor(ProbNegro)
FactorB_ProbGris <- factor(ProbGris)
FactorC_ProbBco <- factor(ProbBco)
Respuesta_CantAciertos<- CantAciertos$CantAciertos
Modelo <- lm(Respuesta_CantAciertos ~ (FactorA_ProbNegro + FactorB_ProbGris+ FactorC_ProbBco)^3)
ANOVA <- aov(Modelo)
summary(ANOVA)
Efectos <- data.frame(FactorA_ProbNegro, FactorB_ProbGris,FactorC_ProbBco, Respuesta_CantAciertos)
Efectos
plot.design(Efectos, fun="mean", ylab= "Aciertos", xlab="Factor")
  