import pandas as pd
import matplotlib.pyplot as plt

url_file = './data/tnueve.xlsx'

h1 = pd.read_excel(url_file,'Hoja1')
#Numeracion=h1['Numeracion'].tolist()
pasos11=h1['PASO1'].tolist()
pasos21=h1['PASO2'].tolist()
pasos31=h1['PASO3'].tolist()
pasos41=h1['PASO4'].tolist()
pasos51=h1['PASO5'].tolist()
pasos61=h1['PASO6'].tolist()
pasos71=h1['PASO7'].tolist()
pasos81=h1['PASO8'].tolist()
pasos91=h1['PASO9'].tolist()

######################################################################


data1 = [pasos11,pasos21,pasos31,pasos41,pasos51,pasos61,pasos71,pasos81, pasos91]

fig1 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig1.add_subplot(111)

plt.xlabel("Pasos")
plt.ylabel("Velocidad")


plt.boxplot(data1)
plt.show()


#########################################################
h2 = pd.read_excel(url_file,'Hoja2')
#Numeracion=h1['Numeracion'].tolist()
pasos12=h2['PASO1'].tolist()
pasos22=h2['PASO2'].tolist()
pasos32=h2['PASO3'].tolist()
pasos42=h2['PASO4'].tolist()
pasos52=h2['PASO5'].tolist()
pasos62=h2['PASO6'].tolist()
pasos72=h2['PASO7'].tolist()
pasos82=h2['PASO8'].tolist()
pasos92=h2['PASO9'].tolist()

######################################################################


data2 = [pasos12,pasos22,pasos32,pasos42,pasos52,pasos62,pasos72,pasos82, pasos92]

fig2 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig2.add_subplot(111)

plt.xlabel("Pasos")
plt.ylabel("Velocidad")


plt.boxplot(data2)
plt.show()



############################################
h3 = pd.read_excel(url_file,'Hoja3')
#Numeracion=h1['Numeracion'].tolist()
pasos13=h3['PASO1'].tolist()
pasos23=h3['PASO2'].tolist()
pasos33=h3['PASO3'].tolist()
pasos43=h3['PASO4'].tolist()
pasos53=h3['PASO5'].tolist()
pasos63=h3['PASO6'].tolist()
pasos73=h3['PASO7'].tolist()
pasos83=h3['PASO8'].tolist()
pasos93=h3['PASO9'].tolist()

######################################################################


data3 = [pasos13,pasos23,pasos33,pasos43,pasos53,pasos63,pasos73,pasos83, pasos93]

fig3 = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig3.add_subplot(111)

plt.xlabel("Pasos")
plt.ylabel("Velocidad")


plt.boxplot(data3)
plt.show()



# Handling missing values of 3rd sheet of an excel file.
#dataframe = pd.read_excel(url_file, na_values="Missing",
                          #sheet_name=2)

#print(dataframe)