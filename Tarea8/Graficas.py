import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url_file = './data/tocho.xlsx'


cuadrado=[]

for i in range(50):
    cuadrado.append(i+1)
print(cuadrado)

h1 = pd.read_excel(url_file,'Hoja1')
#Numeracion=h1['Numeracion'].tolist()
Experimento1=h1['EXPERIMENTO1'].tolist()
Experimento2=h1['EXPERIMENTO2'].tolist()
Experimento3=h1['EXPERIMENTO3'].tolist()
######################################################################
plt.plot(cuadrado, Experimento1, color='red',label='Experimento 1')
plt.plot(cuadrado, Experimento2, color='blue',label='Experimento 2')
plt.plot(cuadrado, Experimento3, color='green',label='Experimento 3')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
plt.xlabel("Tiempo")
plt.ylabel("Proporción de particulas")

#plt.legend(bbox_to_anchor=(0.5, 0.4), loc='upper left', borderaxespad=0.)

plt.show()

########################################################################3




data1 = [Experimento1, Experimento2, Experimento3]

fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data1)

plt.xlabel("Experimento")
plt.ylabel("Proporción de particulas")



plt.show()


#########################################################################
h2 = pd.read_excel(url_file,'Hoja2')
#Numeracion=h1['Numeracion'].tolist()
Experimento12=h2['EXPERIMENTO1'].tolist()
Experimento22=h2['EXPERIMENTO2'].tolist()
Experimento32=h2['EXPERIMENTO3'].tolist()

plt.plot(cuadrado, Experimento12, color='red',label='Experimento 1')
plt.plot(cuadrado, Experimento22, color='blue',label='Experimento 2')
plt.plot(cuadrado, Experimento32, color='green',label='Experimento 3')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
plt.xlabel("Tiempo")
plt.ylabel("Proporción de particulas")

#plt.legend(bbox_to_anchor=(0.5, 0.4), loc='upper left', borderaxespad=0.)

plt.show()
##############################################################

data2 = [Experimento12, Experimento22, Experimento32]

fig2 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig2.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data2)

plt.xlabel("Experimento")
plt.ylabel("Proporción de particulas")

plt.show()



###################################################################33


h3 = pd.read_excel(url_file,'Hoja3')
#Numeracion=h1['Numeracion'].tolist()
Experimento13=h3['EXPERIMENTO1'].tolist()
Experimento23=h3['EXPERIMENTO2'].tolist()
Experimento33=h3['EXPERIMENTO3'].tolist()

plt.plot(cuadrado, Experimento13, color='red',label='Experimento 1')
plt.plot(cuadrado, Experimento23, color='blue',label='Experimento 2')
plt.plot(cuadrado, Experimento33, color='green',label='Experimento 3')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
plt.xlabel("Tiempo")
plt.ylabel("Proporción de particulas")


#plt.legend(bbox_to_anchor=(0.5, 0.4), loc='upper left', borderaxespad=0.)

plt.show()
#############################################################################
data3 = [Experimento13, Experimento23, Experimento33]

fig3 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig3.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data3)

plt.xlabel("Experimento")
plt.ylabel("Proporción de particulas")

plt.show()



###########################################################################
h4 = pd.read_excel(url_file,'Hoja4')
#Numeracion=h1['Numeracion'].tolist()
Experimento14=h4['EXPERIMENTO1'].tolist()
Experimento24=h4['EXPERIMENTO2'].tolist()
Experimento34=h4['EXPERIMENTO3'].tolist()

plt.plot(cuadrado, Experimento14, color='red',label='Experimento 1')
plt.plot(cuadrado, Experimento24, color='blue',label='Experimento 2')
plt.plot(cuadrado, Experimento34, color='green',label='Experimento 3')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
plt.xlabel("Tiempo")
plt.ylabel("Proporción de particulas")

#plt.legend(bbox_to_anchor=(0.5, 0.4), loc='upper left', borderaxespad=0.)

plt.show()
##########################################################################
data4 = [Experimento14, Experimento24, Experimento34]

fig4 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig4.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data4)

plt.xlabel("Experimento")
plt.ylabel("Proporción de particulas")

plt.show()





##########################################################################
h5 = pd.read_excel(url_file,'Hoja5')
#Numeracion=h1['Numeracion'].tolist()
Experimento15=h5['EXPERIMENTO1'].tolist()
Experimento25=h5['EXPERIMENTO2'].tolist()
Experimento35=h5['EXPERIMENTO3'].tolist()

plt.plot(cuadrado, Experimento15, color='red',label='Experimento 1')
plt.plot(cuadrado, Experimento25, color='blue',label='Experimento 2')
plt.plot(cuadrado, Experimento35, color='green',label='Experimento 3')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
plt.xlabel("Tiempo")
plt.ylabel("Proporción de particulas")

#plt.legend(bbox_to_anchor=(0.5, 0.4), loc='upper left', borderaxespad=0.)

plt.show()

data5 = [Experimento15, Experimento25, Experimento35]

fig5 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig5.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data5)

plt.xlabel("Experimento")
plt.ylabel("Proporción de particulas")

plt.show()
