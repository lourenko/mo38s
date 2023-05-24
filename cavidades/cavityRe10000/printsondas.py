
import matplotlib.pyplot as plt
from numpy import linspace, loadtxt
import sys

# Número do caso
try:
    # Próximo argumento depois do nome da função
    nc = sys.argv[1]
except IndexError:
    # Utilize o primeiro valor
    nc = 0

nome = f"postProcessing/sondas/{nc}/U"

datax = loadtxt(f"{nome}x")
datay = loadtxt(f"{nome}y")

t, Ux = datax.T
t, Uy = datay.T

fig, ax = plt.subplots()
ax.plot(t, Ux, 'r-', lw=2, label="$U_x$")
ax.plot(t, Uy, 'b--', lw=2, label="$U_y$")
ax.set_xlabel("$t[s]$")
ax.set_ylabel("$v[m/s]$")

plt.title("Sondas de velocidade")
plt.legend()
plt.show()

