import numpy as np
import matplotlib.pyplot as plt

def fDrawSector(dR, dCenter):
    vtHex = np.zeros(0, dtype=complex)
    for ie in range(6):
        vtHex = np.append(vtHex, dR * (np.cos((ie * np.pi / 3)) + 1j * np.sin((ie * np.pi / 3))))
    vtHex += dCenter
    vtHexp = np.append(vtHex, vtHex[0])
    plt.plot(vtHexp.real, vtHexp.imag, 'k')

# Desenha o setor hexagonal
#fDrawSector(100, 100+50*1j)

# Exibe o gráfico
#plt.axis('equal')  # Define os eixos x e y com mesma escala para garantir proporção correta
#plt.grid(True)  # Habilita a grade de fundo do gráfico (opcional)
#plt.show()