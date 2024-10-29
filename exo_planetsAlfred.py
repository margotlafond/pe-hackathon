import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('PS_2024.10.29_06.31.23.csv', skiprows=96)
mask= (df["soltype"]=="Published Confirmed")
df=df[mask]

#nombre de découvertes par an
df1=df[["pl_name", "disc_year"]]
df1.dropna(subset=['disc_year'])
df1.groupby(["disc_year"]).count().plot()
plt.title('Nombre de découvertes par an, depuis 2014')
plt.xlabel('Année de découverte')
plt.ylabel('Nombre de découvertes')
plt.show()
#Il apparaît sur ce graphique que des étoiles ont principalement été découverte entre 2013 et 2016

#insollation en fonction de la période orbitale 
df2=df[["pl_orbper", "pl_insol"]]
df2=df2.dropna(subset=["pl_orbper", "pl_insol"], how='any')
plt.scatter(df2["pl_orbper"], df2["pl_insol"])
plt.xscale("log")
plt.yscale("log")
plt.xlabel("période orbitale")
plt.ylabel("insollation")
plt.title("Insollation en fonction de la période orbitale")
plt.show()
# Il semblerait qu'il y ait la corrélation suivante: plus la période orbitale augmente, plus l'insollation paraît diminuer 

#masse de la planète en fonction de la masse de l'étoile
mterre=5.9*10**24
df3=df[["pl_bmasse", "st_mass"]]
df3=df3.dropna(subset=["pl_bmasse", "st_mass"], how='any')
df3['pl_bmasse']=df3['pl_bmasse']*mterre
plt.scatter(df3["st_mass"], df3["pl_bmasse"])
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Masse de l'étoile")
plt.ylabel("Masse de la planète")
plt.title("Masse de la planète en fonction de la masse de l'étoile")
plt.show()
#Il semblerait qu'il n'y ait pas vraiment de lien entre la masse de la planète et la masse de son étoile
