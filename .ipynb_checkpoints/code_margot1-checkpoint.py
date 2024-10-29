import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data-planetes.csv', skiprows = 96, index_col = 'pl_name')
df.head(3)

#Année de découverte en fonction de la distance de l'exoplanète à la Terre
plt.scatter(x = df['sy_dist'], y = df['disc_year'], marker = 'o')
plt.title("Année de découverte en fonction de la distance de l'exoplanète à la Terre")
plt.xlabel("Distance de l'exoplanète à la Terre (parsec)")
plt.ylabel("Année de découverte")

#Année de découverte en fonction de la distance de l'exoplanète à la Terre
mask = (df['soltype'] == 'Published Confirmed')
df1 = df[mask]
plt.scatter(x = df1['sy_dist'], y = df1['disc_year'], marker = 'o')
plt.title("Année de découverte en fonction de la distance des exoplanètes confirmées à la Terre")
plt.xlabel("Distance de l'exoplanète à la Terre (parsec)")
plt.ylabel("Année de découverte")

#Rayon de la planète en fonction de sa période orbitale
plt.scatter(x = df1['pl_orbper'], y = df1['pl_rade']*6371000, marker = 'o')
plt.title("Rayon de la planète en fonction de sa période orbitale")
plt.xlabel("Période orbitale (jours)")
plt.ylabel("Rayon de la planète (m)")
plt.xscale('log')
plt.yscale('log')


