import numpy as np
import matplotlib.pyplot as plt
import fDrawDeploy

# Limpa variáveis, limpa tela e fecha todas as figuras
plt.close('all')

# Entrada de parâmetros
dR = 5e3  # Raio do Hexágono

# Cálculos de outras variáveis que dependem dos parâmetros de entrada
dPasso = np.ceil(dR / 10)  # Resolução do grid: distância entre pontos de medição
dIntersiteDistance = 2 * np.sqrt(3 / 4) * dR  # Distância entre ERBs (somente para informação)
dDimX = 5 * dR  # Dimensão X do grid
dDimY = 6 * np.sqrt(3 / 4) * dR  # Dimensão Y do grid

# Vetor com posições das BSs (grid Hexagonal com 7 células, uma célula central e uma camada de células ao redor)
vtBs = [0]
dOffset = np.pi / 6
for iBs in range(2, 8):
    vtBs.append(dR * np.sqrt(3) * np.exp(1j * ((iBs - 2) * np.pi / 3 + dOffset)))
vtBs = np.array(vtBs) + (dDimX / 2 + 1j * dDimY / 2)  # Ajuste de posição das bases (posição relativa ao canto inferior esquerdo)

# Matriz de referência com posição de cada ponto do grid (posição relativa ao canto inferior esquerdo)
dDimY = dDimY + np.mod(dDimY, dPasso)  # Ajuste de dimensão para medir toda a dimensão do grid
dDimX = dDimX + np.mod(dDimX, dPasso)  # Ajuste de dimensão para medir toda a dimensão do grid
mtPosx, mtPosy = np.meshgrid(np.arange(0, dDimX + 1, dPasso), np.arange(0, dDimY + 1, dPasso))

# Calcular os pontos de medição relativos de cada ERB
for iBsD in range(len(vtBs)):  # Loop nas 7 ERBs
    # Matriz 3D com os pontos de medição de cada ERB. Os pontos são modelados como números complexos X + jY,
    # sendo X a posição na abcissa e Y, a posição no eixo das ordenadas
    mtPosEachBS = mtPosx + 1j * mtPosy - vtBs[iBsD]
    # Plot da posição relativa dos pontos de medição de cada ERB individualmente
    plt.figure()
    plt.plot(mtPosEachBS.real, mtPosEachBS.imag, 'bo')
    fDrawDeploy.fDrawDeploy(dR, vtBs - vtBs[iBsD])
    plt.axis('equal')
    plt.title(f'ERB {iBsD + 1}')

plt.show()
