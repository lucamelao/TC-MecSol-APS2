# Dados do material
# Calor específico
# Condutividade térmica
# Coeficiente de transferência por convecção
# Temperatura do fluido
# Temperatura da base
# Raio
# Compriemento
# Delta x
# Tempo total da simulação

from math import *
import numpy as np

# Tolerância 
tol = 1e-10

# Comprimento da aleta (m)
L = 300e-3

# Densidade (kg/mˆ3)
d = 2700

# Condutividade térmica (W/(mK))
k = 180

# Calor específico (J/(kgK))
c = 896

# Temperatura na extremidade
Text = 25

# Temperatura da base
Tb = 100

# Ambiente 
Tinf = 50

# W/mˆK
h = 50

a = k/(d*c)

#C
ct = (h*p/k*Atr)*(Text-Tinf)

# O que eh T?

# Tb e Tl contorno?

# Qual temp

# OUTPUTS
# Gráfico temp x posicao com o resultado numérico
# Gráfico temp x posicao com o resultado analítico