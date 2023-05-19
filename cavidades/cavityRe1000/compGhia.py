
import matplotlib.pyplot as plt
from numpy import linspace, loadtxt

nomeU = "./postProcessing/UemY/60/line.xy"
nomeV = "./postProcessing/VemX/60/line.xy"

ghiauf = "../ghiau.txt"
ghiavf = "../ghiav.txt"

meuU = loadtxt(nomeU)
meuV = loadtxt(nomeV)

y, Ux = meuU.T
x, Uy = meuV.T

ghiaU = loadtxt(ghiauf)
ghiaV = loadtxt(ghiavf)

yg, Uxg = ghiaU.T[0], ghiaU.T[3] # 1ª e 4ª colunas
xg, Uyg = ghiaV.T[0], ghiaV.T[3] # Re = 1000

fig, (ax1, ax2) = plt.subplots(1, 2)
plt.suptitle("Comparação com dados do Ghia (1982)")

ax1.plot(Ux, y, 'b-', lw=2, label="$U_x$")
ax1.plot(Uxg, yg, 'x', lw=2, label="$U_x$ Ghia")
ax1.set_xlabel("$U[m/s]$")
ax1.set_ylabel("$y[m]$")
ax1.legend()

ax2.plot(x, Uy, 'g-', lw=2, label="$U_y$")
ax2.plot(xg, Uyg, '+', lw=2, label="$U_y$ Ghia")
ax2.legend()

plt.show()
