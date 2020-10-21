# install.packages("ggplot2")
library(ggplot2)

undecimal <- c(1,1,1,1,1,1,1,1,1,1)
dosdecimal <- c(1,1,1,1,1,1,1,1,1,1)
tresdecimal <- c(2,9,4,2,4,1,1,2,9,2)
cuatrodecimal <- c(21,17,16,17,83,122,127,10,28,8)
cincodecimal <- c(21,35,63,72,35,7,331,633,56,39)
seisdecimal <- c(260,1456,139,250,125,352,441,1846,581,84)
sietedecimal <- c(37,1145,700,4613,729,777,3744,4974,3254,7251)

library(data.table)


box_df <- data.frame(undecimal,dosdecimal,tresdecimal,cuatrodecimal,cincodecimal,seisdecimal,sietedecimal)


names(box_df)[names(box_df) == 'undecimal'] <- '1'
names(box_df)[names(box_df) == 'dosdecimal'] <- '2'
names(box_df)[names(box_df) == 'tresdecimal'] <- '3'
names(box_df)[names(box_df) == 'cuatrodecimal'] <- '4'
names(box_df)[names(box_df) == 'cincodecimal'] <- '5'
names(box_df)[names(box_df) == 'seisdecimal'] <- '6'
names(box_df)[names(box_df) == 'sietedecimal'] <- '7'
head(box_df)

# Boxplot a partir de un data frame
ggplot(data = stack(box_df), aes(x = ind, y = values)) +
  stat_boxplot(geom = "errorbar", # Bigotes
               width = 0.2) +
  geom_boxplot(fill = "#4271AE", colour = "#1F3552", # Colores
               alpha = 0.8, outlier.colour = "red") +
  scale_y_continuous(name = "Cantidad de dimensiones",breaks=seq(0, 7000, 1000)) +  # Etiqueta de la variable continua
  
  scale_x_discrete(name = "Decimales") +        # Etiqueta de los grupos
  ggtitle(" ") +   # Título del plot
  theme(axis.line = element_line(colour = "black", # Personalización del tema
                                 size = 0.25))

