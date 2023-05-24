#############################################
#
# Plota os dados da pasta teste para cada
# um dos arquivos alí depositados.
#
#############################################

import os, sys          # Pastas e arquivos
import numpy as np           # Vetores
import matplotlib.pyplot as plt # Gráficos

# Salvar as pastas dentro da lista 'pastas'
pasteste = str(sys.argv[1]) # Passaremos o
# nome da pasta de testes via linha de comando
pastas = os.listdir(pasteste)

cor = 'C0'

# Figura para o gráfico
fig, ax1 = plt.subplots()
ax1.set_xlabel('$x[m]$')
ax1.set_ylabel('$v[m/s]$')
ax1.tick_params(axis='y', colors=cor)
ax1.yaxis.label.set_color(cor)
ax1.tick_params(axis='x', colors=cor)
ax1.xaxis.label.set_color(cor)
axt = ax1.twinx()
axt.set_ylabel('$y[m]$')
ax2 = axt.twiny()
ax2.set_xlabel('$u[m/s]$')

tipos = ['-', '--', '-.', ':', 'dashedcondensed']

for ip, pasta in enumerate(pastas):
    # U variando em y
    arquy = pasteste+f'/{pasta}/UemY'
    datuy = np.loadtxt(arquy)
    y, u = datuy.T # Colunas transpostas

    # V variando em x
    arqvx = pasteste+f'/{pasta}/VemX'
    datvx = np.loadtxt(arqvx)
    x, v = datvx.T

    ax1.plot(x, v, ls=tipos[ip], c=cor, label=pasta)
    ax2.plot(u, y, ls=tipos[ip], c='0.3')


fig.tight_layout()
fig.legend()
plt.show()

