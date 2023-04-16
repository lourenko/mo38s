#############################################
#
# Plota os dados da pasta teste para cada
# um dos arquivos alí depositados.
#
#############################################

import os                  # Pastas e arquivos
import numpy as np           # Vetores
import matplotlib.pyplot as plt # Gráficos

# Salvar as pastas dentro da lista 'pastas'
pastas = os.listdir('testes')

# Figura para o gráfico
fig, ax1 = plt.subplots()
ax2 = ax1.twinx().twiny()

for pasta in pastas:
    # U variando em y
    arquy = r'testes/'+pasta+r'/uemy'
    datuy = np.loadtxt(arquy)
    y, u = datuy.T # Colunas transpostas

    # V variando em x
    arqvx = r'testes/'+pasta+r'/vemx'
    datvx = np.loadtxt(arqvx)
    x, v = datvx.T

    ax1.plot(x, v, c='C0')
    ax2.plot(u, y, c='C1')


fig.tight_layout()
plt.show()

