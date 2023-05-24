#############################################
#
# Plota os dados da pasta teste para cada
# um dos arquivos alí depositados.
#
#############################################

import os, sys, shutil          # Pastas e arquivos
# import numpy as np           # Vetores
# import matplotlib.pyplot as plt # Gráficos

# Salvar as pastas dentro da lista 'pastas'
pasta = str(sys.argv[1]) # Passaremos o

num = str(sys.argv[2])
if float(num) < 1:
    num = None

if len(sys.argv) > 3:
    destino = str(sys.argv[3])
else:
    destino = "comparaRe100"

caminho = f"{pasta}/postProcessing/"
valores = os.listdir(caminho)

for arq1 in valores:
    if not num:
        resultados = os.listdir(f"{caminho}{arq1}")
        resultados.sort(key=float)
        num = resultados[-1]

    diret = f"{caminho}{arq1}/{num}"

    pastanova = f"{destino}/{pasta}"
    if not os.path.exists(pastanova):
        os.mkdir(pastanova)

    for arq2 in os.listdir(diret):
        shutil.copy2(f"{diret}/{arq2}",f"{pastanova}/{arq1}")

