import pandas as pd
import matplotlib.pyplot as plt
url_file = './data/Resultados.xlsx'

embalse1 = pd.read_excel(url_file,'Faciles_1')
Nucleos1=embalse1['Nucleos'].tolist()
Ascendente1=embalse1['Ascendente'].tolist()
Descendente1=embalse1['Descendente'].tolist()
Aleatorio1=embalse1['Aleatorio'].tolist()

embalse2 = pd.read_excel(url_file,'Dificil_1')
Nucleos2=embalse2['Nucleos'].tolist()
Ascendente2=embalse2['Ascendente'].tolist()
Descendente2=embalse2['Descendente'].tolist()
Aleatorio2=embalse2['Aleatorio'].tolist()

plt.plot(Nucleos1,Ascendente1,label="Ascendente")
plt.plot(Nucleos1,Descendente1,label="Descendente")
plt.plot(Nucleos1,Aleatorio1,label="Aleatorio")
plt.xlabel('Núcleos')
plt.ylabel('Tiempo (seg)')
plt.title('Trabajos Faciles')
plt.legend()
plt.show()
plt.close()

plt.plot(Nucleos2,Ascendente2,label="Ascendente")
plt.plot(Nucleos2,Descendente2,label="Descendente")
plt.plot(Nucleos2,Aleatorio2,label="Aleatorio")
plt.xlabel('Núcleos')
plt.ylabel('Tiempo (seg)')
plt.title('Trabajos Difis')
plt.legend()
plt.show()
plt.close()