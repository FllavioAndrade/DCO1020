import numpy as np
import Entrega_03
def calculate_outage_rate(dFc,tipo, dR):
    # Entrada de parâmetros
    dOutRate = 200

    while dOutRate > 10:
        # Cálculos de outras variáveis que dependem dos parâmetros de entrada
        dPasso = np.ceil(dR / 50)  # Resolução do grid: distância entre pontos de medição
        dRMin = dPasso
        dIntersiteDistance = 2 * np.sqrt(3 / 4) * dR  # Distância entre ERBs (somente para informação)
        dDimX = 5 * dR  # Dimensão X do grid
        dDimY = 6 * np.sqrt(3 / 4) * dR  # Dimensão Y do grid
        dPtdBm = 57  # EIRP (incluindo ganho e perdas) (https://pt.slideshare.net/naveenjakhar12/gsm-link-budget)
        dPtLinear = 10 ** (dPtdBm / 10) * 1e-3  # EIRP em escala linear
        dSensitivity = -104  # Sensibilidade do receptor (http://www.comlab.hut.fi/opetus/260/1v153.pdf)
        dHMob = 5  # Altura do receptor
        dHBs = 30  # Altura do transmissor
        dAhm = 3.2 * (np.log10(11.75 * dHMob)) ** 2 - 4.97  # Modelo Okumura-Hata: Cidade grande e fc  >= 400MHz

        # Vetor com posições das BSs (grid Hexagonal com 7 células, uma célula central e uma camada de células ao redor)
        vtBs = np.array([0])
        dOffset = np.pi / 6
        for iBs in range(2, 8):
            vtBs = np.append(vtBs, dR * np.sqrt(3) * np.exp(1j * ((iBs - 2) * np.pi / 3 + dOffset)))
        vtBs = vtBs + (dDimX / 2 + 1j * dDimY / 2)  # Ajuste de posição das bases (posição relativa ao canto inferior esquerdo)

        # Matriz de referência com posição de cada ponto do grid (posição relativa ao canto inferior esquerdo)
        dDimY = np.ceil(dDimY + np.mod(dDimY, dPasso))  # Ajuste de dimensão para medir toda a dimensão do grid
        dDimX = np.ceil(dDimX + np.mod(dDimX, dPasso))  # Ajuste de dimensão para medir toda a dimensão do grid
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
                mtPldB = 46.3 + 33.9 * np.log10(dFc) - 13.82*np.log10(dHBs) - dAhm + (44.9 - 6.55*np.log10(dHBs)) * np.log10(mtDistEachBs / 1e3) \
                         + 3
            mtPowerEachBSdBm = dPtdBm - mtPldB  # Potências recebidas em cada ponto de medição

            # Cálulo da maior potência em cada ponto de medição
            mtPowerFinaldBm = np.maximum(mtPowerFinaldBm, mtPowerEachBSdBm)

        # Outage (limite 10%)
        dOutRate = 100 * np.sum(mtPowerFinaldBm < dSensitivity) / np.size(mtPowerFinaldBm)
        #print(dOutRate)
        dR = dR - 10
    return dOutRate, dR


continuar = 1
while (continuar == 1):
    vtFc = [800, 900, 1800, 1900, 2100]
    print("\nModelo de propagação de onda")
    tipo = 4
    opcao =4
    dR = 1

    while (opcao < 1 or opcao > 2):# or (dR < 1000):
        opcao = int(input("1.Cálculo de Outage de potência\n2.Cálculo da potência recebida nos pontos de medição do REM de cada ERB\n"))
        if opcao == 1 or opcao == 2:
            while (tipo < 1 or tipo > 2) or (dR < 1000):
                tipo = int(input("Escolha o modelo de propagação\n\n1.Okumura-Hata\n2.COST 231\n"))
                dR = int(input("Digite o Raio do Hexágono em metros (m)\n"))

                if (tipo < 1 or tipo > 2):
                    print("Valor Inválido para o modelo de propagação!\n")
                if dR < 1000:
                    print("Valor Inválido para o Raio do Hexágono\n")

        if opcao == 2:
            frequence = 6
            while (frequence < 1 or frequence > 5):
                frequence = int(input("Escolha a frequencia:\n1 - 800Mhz\n2 - 900Mhz\n3 - 1800Mhz\n4 - 1900Mhz\n5 - 2100Mhz\n"))
                if frequence == 1:
                    valueFrequence = 800
                elif frequence == 2:
                    valueFrequence = 900
                elif frequence == 3:
                    valueFrequence = 1800
                elif frequence == 4:
                    valueFrequence = 1900
                elif frequence == 2:
                    valueFrequence = 2100

                if frequence >= 1 and frequence <= 5:
                    Entrega_03.calcPower(dR, valueFrequence, tipo)

        elif opcao == 1:
            if tipo == 1:
                modelo = "Okumura-Hata"
            elif tipo == 2:
                modelo = 'COST Hata (COST 231)'

            for dFc in vtFc:
                dOutRate = calculate_outage_rate(dFc, tipo, dR)
                print(modelo)
                print(f'----------------------- ')
                print(f'Frequência da portadora = {dFc}MHz')
                print(f'Taxa de outage = {dOutRate[0]:.4f}%')
                print(f'Raio do Hexágono = {dOutRate[1] + 10}m\n')

    continuar = int(input("1. Continuar\n2. Sair\n"))