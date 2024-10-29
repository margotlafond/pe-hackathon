import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data-planetes.csv', skiprows = 96, index_col = 'pl_name')
df.head(3)

#Année de découverte en fonction de la distance de l'exoplanète CONFIRME à la Terre
mask = (df['soltype'] == 'Published Confirmed')
df1 = df[mask]
plt.scatter(x = df1['sy_dist'], y = df1['disc_year'], marker = 'o')
plt.title("Année de découverte en fonction de la distance des exoplanètes confirmées à la Terre")
plt.xlabel("Distance de l'exoplanète à la Terre (parsec)")
plt.ylabel("Année de découverte")

#Année de découverte en fonction de la distance de l'exoplanète CONFIRME à la Terre - avec couleurs
decouv = df['discoverymethod'].unique()
couleurs = ['black', 'lightcoral', 'chocolate', 'darkorange', 'yellow', 'palegreen', 'darkgreen', 'turquoise', 'dodgerblue', 'darkviolet', 'fuchsia']
for i in range(len(decouv)) :
    mask_dec = (df1['discoverymethod'] == decouv[i])
    df2 = df1[mask_dec]
    plt.scatter(x = df2['sy_dist'], y = df2['disc_year'], marker = 'o', s = 10,  label = decouv[i], color = couleurs[i])
plt.title("Année de découverte en fonction de la distance des exoplanètes confirmées à la Terre - couleurs")
plt.xlabel("Distance de l'exoplanète à la Terre (parsec)")
plt.ylabel("Année de découverte")
plt.legend(fontsize = 7, title = 'Méthode de découverte')
plt.show()

# +
# COMMENTAIRE : les exoplanètes les plus lointaines sont celles qui ont été découvertes le plus tard => perfectionnement appareils
# On remarque aussi que de plus en plus de planètes sont découvertes au fil des ans, que la méthode "Transit" 
# permet de découvrir les planètes plutôt proches de la Terre tandis que "Microlensing" permet d'explorer plus loin de la Terre.
# -

#Rayon de la planète en fonction de sa période orbitale
plt.scatter(x = df1['pl_orbper'], y = df1['pl_rade']*6371000, marker = 'o', s=10)
plt.title("Rayon de la planète en fonction de sa période orbitale")
plt.xlabel("Période orbitale (jours)")
plt.ylabel("Rayon de la planète (m)")
plt.xscale('log')
plt.yscale('log')

# +
#Rayon de la planète en fonction de sa période orbitale - couleurs

for i in range(len(decouv)) :
    mask_dec = (df1['discoverymethod'] == decouv[i])
    df3 = df1[mask_dec]
    plt.scatter(x = df3['pl_orbper'], y = df3['pl_rade']*6371000, marker = 'o', s = 5,  label = decouv[i], color = couleurs[i])
plt.title("Rayon de la planète en fonction de sa période orbitale - couleurs")
plt.xlabel("Période orbitale (jours)")
plt.ylabel("Rayon de la planète (m)")
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize = 7, title = 'Méthode de découverte')
plt.show()

# +
# COMMENTAIRE : à première vue, pas de lien

# +
#Magnitude en fonction du rayon - couleurs

for i in range(len(decouv)) :
    mask_dec = (df1['discoverymethod'] == decouv[i])
    df3 = df1[mask_dec]
    plt.scatter(y = df3['sy_gaiamag'], x = df3['pl_rade']*6371000, marker = 'o', s = 5,  label = decouv[i], color = couleurs[i])
plt.title("Magnitude en fonction du rayon - couleurs")
plt.ylabel("Magnitude")
plt.xlabel("Rayon de la planète (m)")
plt.xscale('log')
plt.yscale('log')
plt.legend(loc = 'best', fontsize = 7, title = 'Méthode de découverte')
plt.show()

# +
# COMMENTAIRE : à première vue, pas de lien
