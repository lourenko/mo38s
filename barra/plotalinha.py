# plotalinha.py

import numpy as np
import matplotlib.pyplot as plt

arquivo = "postProcessing/amostras/0.09/line.xy"
with open(arquivo) as arq:
    dados = np.loadtxt(arq)
    x = dados[::,:1:]*1000 # Transforma em [mm]
    y = dados[::,1::]

fig, ax = plt.subplots()
ax.plot(x, y, c="C4")
ax.set_xlabel(r'$x$[mm]')
ax.set_ylabel(r'$T$[K]')
plt.show()

