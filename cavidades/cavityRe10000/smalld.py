#------------------------------#
# Determine o valor da menor
# célula em uma malha refinada.
#------------------------------#

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import root


def delta(R, L, N):
    """
    Retorna dx da menor célula
    R: taxa de refinamento
    L: Comprimento no refino
    N: Número de células
    """
    r = pow(R, 1/(N-1))
    alfa = R
    if R < 1:
        alfa = 1 - pow(r,-1) + pow(r,-N)
    dx = L*(r-1)/(alfa*r - 1)
    return dx

L = 0.5 # m
N = 24  # volumes
d = -1/72
f = lambda R: delta(R, L, N) - d 
R = root(f, 0.3, method='krylov', tol=1e-10)
print(R.x, 1/R.x, d, delta(R.x, L, N))


#Rlista = np.linspace(0.1, 4, 4096)
#Delta = [delta(R, 1.0, 48) for R in Rlista]
#plt.plot(Rlista, Delta)
#plt.show()

