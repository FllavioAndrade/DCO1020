import numpy as np
import matplotlib.pyplot as plt

import fDrawDeploy

def calcPower (dR, dFc, tipo):
    #dR = 5e3  # Raio do Hexágono
    #dFc = 800  # Frequência da portadora MHz
    # Cálculos de outras variáveis que dependem dos parâmetros de entrada
    dPasso = np.ceil(dR / 10)  # Resolução do grid: distância entre pontos de medição
    dRMin = dPasso  # Raio de segurança
    dIntersiteDistance = 2 * np.sqrt(3 / 4) * dR  # Distância entre ERBs (somente para informação)
    dDimX = 5 * dR  # Dimensão X do grid
    dDimY = 6 * np.sqrt(3 / 4) * dR  # Dimensão Y do grid
    dPtdBm = 57  # EIRP (incluindo ganho e perdas) (https://pt.slideshare.net/naveenjakhar12/gsm-link-budget)
    dPtLinear = 10 ** (dPtdBm / 10) * 1e-3  # EIRP em escala linear
    dHMob = 5  # Altura do receptor
    dHBs = 30  # Altura do transmissor
    dAhm = 3.2 * (np.log10(11.75 * dHMob)) ** 2 - 4.97  # Modelo Okumura-Hata: Cidade grande e fc  >= 400MHz

    # Vetor com posições das BSs (grid Hexagonal com 7 células, uma célula central e uma camada de células ao redor)
    vtBs = np.array([0], dtype=complex)
    dOffset = np.pi / 6
    for iBs in range(2, 8):
        vtBs = np.append(vtBs, dR * np.sqrt(3) * np.exp(1j * ((iBs - 2) * np.pi / 3 + dOffset)))
    vtBs += (dDimX / 2 + 1j * dDimY / 2)  # Ajuste de posição das bases (posição relativa ao canto inferior esquerdo)

    # Matriz de referência com posição de cada ponto do grid (posição relativa ao canto inferior esquerdo)
    dDimY += np.mod(dDimY, dPasso)  # Ajuste de dimensão para medir toda a dimensão do grid
    dDimX += np.mod(dDimX, dPasso)  # Ajuste de dimensão para medir toda a dimensão do grid
    mtPosx, mtPosy = np.meshgrid(np.arange(0, dDimX + 1, dPasso), np.arange(0, dDimY + 1, dPasso))

    # Iniciação da Matriz de com a potência de recebida máxima em cada ponto
    # medido. Essa potência é a maior entre as 7 ERBs.
    mtPowerFinaldBm = -np.inf * np.ones_like(mtPosy)

    # Calcular O REM de cada ERB e acumular a maior potência em cada ponto de medição
    for iBsD in range(len(vtBs)):  # Loop nas 7 ERBs
        # Matriz 3D com os pontos de medição de cada ERB. Os pontos são modelados como números complexos X + jY,
        # sendo X a posição na abcissa e Y, a posição no eixo das ordenadas
        mtPosEachBS = mtPosx + 1j * mtPosy - vtBs[iBsD]
        mtDistEachBs = np.abs(mtPosEachBS)  # Distância entre cada ponto de medição e a sua ERB
        mtDistEachBs[mtDistEachBs < dRMin] = dRMin  # Implementação do raio de segurança

        if tipo == 1:
            # Okumura-Hata (cidade urbana) - dB
            mtPldB = 69.55 + 26.16 * np.log10(dFc) + (44.9 - 6.55 * np.log10(dHBs)) * np.log10(mtDistEachBs / 1e3) \
                 - 13.82 * np.log10(dHBs) - dAhm
        else:
            # Cost 231
            mtPldB = 46.3 + 33.9 * np.log10(dFc) - 13.82 * np.log10(dHBs) - dAhm + (
                        44.9 - 6.55 * np.log10(dHBs)) * np.log10(mtDistEachBs / 1e3) \
                     + 3
        mtPowerEachBSdBm = dPtdBm - mtPldB  # Potências recebidas em cada ponto de medição

        # Cálulo da maior potência em cada ponto de medição
        mtPowerFinaldBm = np.maximum(mtPowerFinaldBm, mtPowerEachBSdBm)

        # Plot da REM de cada ERB individualmente
        plt.figure()
        plt.pcolor(mtPosx, mtPosy, mtPowerEachBSdBm)
        plt.colorbar()
        # Desenha setores hexagonais
        fDrawDeploy.fDrawDeploy(dR, vtBs)
        plt.axis('equal')
        plt.title(f'ERB {iBsD + 1}')

    # Plot da REM de todo o grid (composição das 7 ERBs)
    plt.figure()
    plt.pcolor(mtPosx, mtPosy, mtPowerFinaldBm)
    plt.colorbar()
    fDrawDeploy.fDrawDeploy(dR, vtBs)
    plt.axis('equal')
    plt.title('Todas as 7 ERB')

    plt.show()

#calcPower(5e3, 800, 1)
