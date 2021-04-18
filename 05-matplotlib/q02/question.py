##
##  Graficacion usando Matplotlib
##  ===========================================================================
##
##  Construya una gráfica similar a la presentada en el archivo `original.png`
##  usando el archivo `data.csv`. La gráfica generada debe salvarse en el 
##  archivo `generada.png`. 
##
##  Salve la figura al disco con:
##
##     plt.savefig('generada.png')
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import os
df=pd.read_csv(open('data.csv'), delimiter=',')
copia = df.copy()
(df.loc[df['Region'] == "Asia", "Region"]) = "Asia"
aux = (df.groupby('Region')['Poblacion 0-14','Poblacion 15-64','Poblacion 65+'].sum()).sort_values(by='Region')
auxT = aux.T
fig,axs = plt.subplots(1, 6, sharex='col', sharey='row', figsize=(13, 6), dpi=72)
plt.subplots_adjust(wspace = 0, hspace=0.1)
plt.setp(axs[0], ylabel='Poblacion')
plt.style.use('default')
colors = ['tab:orange', 'tab:blue', 'tab:green']
for i, colname in enumerate(auxT.columns):
    axs[i].bar(list(auxT.index), auxT[colname], color=colors)
    axs[i].set_title(colname)
    plt.style.use('default')
    for tick in axs[i].get_xticklabels():
        tick.set_rotation(90)
plt.tight_layout()
plt.savefig('generada.png')