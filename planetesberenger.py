import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("excel_planetes.csv", skiprows=96, index_col="pl_name")
mask = (df['soltype'] == 'Published Confirmed')
df = df[mask]

df1 = df[['pl_eqt','pl_orbsmax']]
df1 = df1.dropna(axis=0,how='any')
plt.scatter(x=df1['pl_eqt'],y=df1['pl_orbsmax'],marker='.')
plt.title('Demi-grand axe en fonction de la temperature')
plt.xlabel('Demi-grand axe (au)')
plt.ylabel('Temperature (K)')
plt.yscale('log')
plt.show()

# +
decouv = df['discoverymethod'].unique()
couleurs = ['black', 'lightcoral', 'chocolate', 'darkorange', 'yellow', 'palegreen', 'darkgreen', 'turquoise', 'dodgerblue', 'darkviolet', 'fuchsia']
for i in range(len(decouv)) :
    mask_dec = (df['discoverymethod'] == decouv[i])
    df11 = df[mask_dec]
    plt.scatter(x=df11['pl_eqt'],y=df11['pl_orbsmax'],marker='.', s = 10,  label = decouv[i], color = couleurs[i])

plt.title('Demi-grand axe en fonction de la temperature')
plt.xlabel('Demi-grand axe (au)')
plt.ylabel('Temperature (K)')
plt.yscale('log')
plt.legend()
plt.show()
# -

df2 = df[['pl_orbper','pl_orbeccen']]
df2 = df2.dropna(axis=0,how='any')
plt.scatter(x=df['pl_orbper'],y=df['pl_orbeccen'],marker='.')
plt.title('Excentricite en fonction de la periode orbitale')
plt.xlabel('Periode orbitale (jours)')
plt.ylabel('Excentricite')
plt.xscale('log')
plt.show()


# +
decouv = df['discoverymethod'].unique()
couleurs = ['black', 'lightcoral', 'chocolate', 'darkorange', 'yellow', 'palegreen', 'darkgreen', 'turquoise', 'dodgerblue', 'darkviolet', 'fuchsia']
for i in range(len(decouv)) :
    mask_dec = (df['discoverymethod'] == decouv[i])
    df11 = df[mask_dec]
    plt.scatter(x=df11['pl_orbper'],y=df11['pl_orbeccen'],marker='.', s = 10,  label = decouv[i], color = couleurs[i])

plt.title('Excentricite en fonction de la periode orbital')
plt.xlabel('Periode orbitale (jours)')
plt.ylabel('Excentricite')
plt.xscale('log')
plt.legend()
plt.show()
# -

df3 = df[['pl_rade','pl_bmasse']]
df3 = df3.dropna(axis=0,how='any')
plt.scatter(x=df['pl_bmasse'],y=df['pl_rade'],marker='.')
plt.title('Rayon en fonction de la masse')
plt.xlabel('Masse (earth mass)')
plt.ylabel('Rayon (earth radius)')
plt.xscale('log')
plt.yscale('log')
plt.show()

# +
decouv = df['discoverymethod'].unique()
couleurs = ['black', 'lightcoral', 'chocolate', 'darkorange', 'yellow', 'palegreen', 'darkgreen', 'turquoise', 'dodgerblue', 'darkviolet', 'fuchsia']
for i in range(len(decouv)) :
    mask_dec = (df['discoverymethod'] == decouv[i])
    df11 = df[mask_dec]
    plt.scatter(x=df11['pl_rade'],y=df11['pl_bmasse'],marker='.', s = 10,  label = decouv[i], color = couleurs[i])

plt.title('Rayon en fonction de la masse')
plt.xlabel('Masse (earth mass)')
plt.ylabel('Rayon (earth radius)')
plt.xscale('log')
plt.yscale('log')
plt.legend(fontsize=7, title='Methode de decouverte')
plt.show()
# -


    
