library(ggplot2)

pv <- c(0,	0,	0,	0,	0,	0.1,	0.1,	0.1,	0.1,	0.1,	0.2,	0.2,	0.2,	0.2,	0.2,	0.3,	
          0.3,	0.3,	0.3,	0.3,	0.4,	0.4,	0.4,	0.4,	0.4,	0.5,	0.5,	0.5,	0.5,	0.5,
          0.6,	0.6,	0.6,	0.6,	0.6,	0.7,	0.7,	0.7,	0.7,	0.7,	0.8,	0.8,	0.8,	0.8,
          0.8,	0.9,	0.9,	0.9,	0.9,	0.9,	1,	1,	1,	1,	1)



maxInfec <- c(54,	88,	62,	56,	66,	2,	46,	48,	60,	64,	60,	32,	54,	66,
            0, 4,	54,	46,	42,	44,	28,	42,	20,	36,	38,	20,	30,	16,
            28,	14,	22,	18,	22,	8,	34,	8,	20,	4,	10,	2,	12,	6,
            2,	10,	10,	2,	12,	10,	10,	6,	4,	2,	6,	0,	6)


tiemMaxInfec <- c(34,	54,	52,	59,	39,	0,	79,	43,	36,	37,	37,	41,	49,	52,	0,	0,	34,	61,	50,	98,
                  94,	62,	74,	63,	42,	64,	35,	50,	29,	33,	94,	30,	96,	89,	31,	47,	69,	0,	8,	0,
                  1,	22,	0,	62,	8,	0,	42,	4,	23,	0,	0,	0,	0,	0,	0)


tiemSinConta <- c(99,	99,	99,	99,	99,	5,	99,	99,	99,	99,	99,	99,	99,	99,	0,	17,	99,	99,	99,	99,	99,
                  99,	99,	99,	99,	99,	99,	99,	99,	99,	99,	99,	99,	99,	99,	99,	99,	99,	99,	21,	99,	99,
                  28,	99,	99,	24,	99,	74,	99,	85,	32,	86,	54,	0,	72)
 
df <- data.frame(pv, maxInfec, tiemMaxInfec, tiemSinConta)
head(df)

ggplot(data = df,
       mapping = aes(x =pv,
                     y = maxInfec)) +
  geom_point()+
  scale_x_continuous(name = "Probabilidad de Vacunación (Pv)",breaks = seq(0, 1, by = 0.10))+
  scale_y_continuous(name = "% Máximo de Infectados",breaks = seq(0, 110, by = 10))+
  theme(axis.line = element_line(colour = "black", # Personalización del tema
                                 size = 0.25))
  
ggplot(data = df,
       mapping = aes(x =pv,
                     y = tiemMaxInfec)) +
  geom_point()+
  scale_x_continuous(name = "Probabilidad de Vacunación (Pv)",breaks = seq(0, 1, by = 0.10))+
  scale_y_continuous(name = "Momento de alcance del % Máximo de Infectados",breaks = seq(0, 120, by = 20))+
  theme(axis.line = element_line(colour = "black", # Personalización del tema
                                 size = 0.25))

ggplot(data = df,
       mapping = aes(x =pv,
                     y = tiemSinConta)) +
  geom_point()+
  scale_x_continuous(name = "Probabilidad de Vacunación (Pv)",breaks = seq(0, 1, by = 0.10))+
  scale_y_continuous(name = "Momento de alcance de 0 contagios",breaks = seq(0, 120, by = 20))+
  theme(axis.line = element_line(colour = "black", # Personalización del tema
                                 size = 0.25))
