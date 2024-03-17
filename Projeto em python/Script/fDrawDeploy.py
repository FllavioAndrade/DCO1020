import matplotlib.pyplot as plt
import numpy as np
import fDrawSector
def fDrawDeploy(dR, vtBs):
    # Desenha setores hexagonais
    for iBsD in range(len(vtBs)):
        fDrawSector.fDrawSector(dR, vtBs[iBsD])
    # Plot BSs
    plt.plot(vtBs.real, vtBs.imag, 'sk')
    plt.axis('equal')

# Exemplo de coordenadas para 3 BSs
#vtBs = np.array([100+15j, 250 +100j, 100+190j])

# Desenha a implantação com raio 100
#fDrawDeploy(100, vtBs)

# Exibe o gráfico final
#plt.show()