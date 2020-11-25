import pandas as pd
import matplotlib.pyplot as plt

url_file = './data/tdiez.xlsx'



h1 = pd.read_excel(url_file,'Original')
#Numeracion=h1['Numeracion'].tolist()
g1=h1['GAP100'].tolist()
f1=h1['mejorEntontrado/tiempoUtilizado'].tolist()

data1 = [g1]

fig1 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax1 = fig1.add_subplot(111)

# Create the boxplot
bp1 = ax1.boxplot(data1)


plt.ylabel("% de diferencia entre el optimo y la mejor solución encontrada ")



plt.show()

data2 = [f1]
fig2 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax2 = fig2.add_subplot(111)

# Create the boxplot
bp2 = ax2.boxplot(data2)


plt.ylabel("valor que se aporta a una función objetivo por segundo de ejecución ")



plt.show()

####################################333333

h2 = pd.read_excel(url_file,'Ruleta')
#Numeracion=h1['Numeracion'].tolist()
g3=h2['GAP100'].tolist()
f3=h2['mejorEntontrado/tiempoUtilizado'].tolist()

data3 = [g3]

fig3 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax3 = fig3.add_subplot(111)

# Create the boxplot
bp3 = ax3.boxplot(data3)


plt.ylabel("% de diferencia entre el optimo y la mejor solución encontrada ")



plt.show()

data4 = [f3]
fig4 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax4 = fig4.add_subplot(111)

# Create the boxplot
bp4 = ax4.boxplot(data4)


plt.ylabel("valor que se aporta a una función objetivo por segundo de ejecución ")



plt.show()