import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#découverte de la table de données 
df = pd.read_csv("données.csv", skiprows=96)
df.head(3)

#caractéristique de la table
print(df.shape)
df.columns

# +
#tracé de la masse de l'exoplanète en fonction de la période orbitale

#1er étape: création du tableau nécessaire pour tracer le graphique
mass = df[ df['soltype'] == 'Published Confirmed' ][['pl_bmassj', 'pl_orbper', 'discoverymethod']] #on sélectionne les colonnes qui nous interesse en considérant que les planètes confirmées
print('nombre de données manquantes:')
print(mass.isna().sum())
mass = mass.dropna(how='any') #on enlève les lignes avec données manquantes
mass['pl_bmassj'] = mass['pl_bmassj'] * 1.8986 * 10**27 #on transforme la donnée en kg
print('forme du tableau final:')
print(mass.shape)
mass.columns = ['mass', 'orbit', 'discoverymethod']
mass.head(3)
# -

#tracé du graphique
plt.scatter(y=mass['mass'], x=mass['orbit'], marker='o')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('mass')
plt.xlabel('orbit')
plt.title('Masse en kg en fonction de la période orbitale en jour')
plt.show()

decouv = df['discoverymethod'].unique()
couleurs = ['black', 'lightcoral', 'chocolate', 'darkorange', 'yellow', 'palegreen', 'darkgreen', 'turquoise', 'dodgerblue', 'darkviolet', 'fuchsia']
for i in range(len(decouv)) :
    mask_dec = (mass['discoverymethod'] == decouv[i])
    df2 = mass[mask_dec]
    plt.scatter(x = df2['orbit'], y = df2['mass'], marker = 'o', s = 10,  label = decouv[i], color = couleurs[i])
plt.title("Année de découverte en fonction de la distance des exoplanètes confirmées à la Terre - couleurs")
plt.xlabel("Distance de l'exoplanète à la Terre (parsec)")
plt.ylabel("Année de découverte")
plt.legend(fontsize = 5, title = 'moyen de découvert')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('mass')
plt.xlabel('orbit')
plt.title('Masse en kg en fonction de la période orbitale en jour')
plt.show()

# +
#commentaire des graphiques: les planètes les plus lourdes ont une période orbitale plus longue
# -

annee = df[ df['soltype'] == 'Published Confirmed' ][['disc_year', 'sy_gaiamag', 'discoverymethod']]
annee = annee.dropna(how='any')
plt.scatter(x=annee['sy_gaiamag'], y=annee['disc_year'], marker='o')
plt.ylabel('annee')
plt.xlabel('magnitude')
plt.title('Année de découverte en fonction de la magnitude (plus la magnitude est faible plus c est visible dans le ciel')
plt.show()

decouv = df['discoverymethod'].unique()
couleurs = ['black', 'lightcoral', 'chocolate', 'darkorange', 'yellow', 'palegreen', 'darkgreen', 'turquoise', 'dodgerblue', 'darkviolet', 'fuchsia']
for i in range(len(decouv)) :
    mask_dec = (annee['discoverymethod'] == decouv[i])
    df2 = annee[mask_dec]
    plt.scatter(x = df2['sy_gaiamag'], y = df2['disc_year'], marker = 'o', s = 10,  label = decouv[i], color = couleurs[i])
plt.title("Année de découverte en fonction de la distance des exoplanètes confirmées à la Terre - couleurs")
plt.xlabel("Distance de l'exoplanète à la Terre (parsec)")
plt.ylabel("Année de découverte")
plt.legend(fontsize = 5, title = 'moyen de découvert')
plt.ylabel('annee')
plt.xlabel('magnitude')
plt.title('Année de découverte en fonction de la magnitude (plus la magnitude est faible plus c est visible dans le ciel')
plt.show()

# +
# commentaire du graphique: on remarque que les systèmes les plus lumineux (faible magnitude) sont les premiers à avoir été découverts
# de plus, on remarque que la méthode de découverte différe selon si les systèmes sont plus (magnitude faible) ou moins lumineux (magnitude élevé) 
#l'apparition de la méthode par transit a permis de découvrir des systèmes de magnitude beaucoup plus élevé !
