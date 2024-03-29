
# Hands-on 01: Uso de modelos de propagação para análises sistêmicas

## Parte 01: Avaliação de cobertura celular


### Visão Geral
Este programa implementa um modelo de propagação de onda para calcular a taxa de outage e a potência recebida em pontos de medição. O modelo considera um cenário com 7 células hexagonais e utiliza o modelo de Okumura-Hata ou COST 231 para calcular o Path Loss.
### Objetivos

- Criar um Grid Hexagonal para modelar cobertura de Estações Rádio Base;
- Analisar potência recebida visualmente por meio de Radio Environment Maps (REMs);
- Fazer exemplo de estudo de Outage de potência.

### Dependências
- Python 3.x
- numpy: Uma poderosa biblioteca para cálculos numéricos em Python.
- Matplotlib: biblioteca Python amplamente utilizada para criação de gráficos estáticos, animados e interativos.

<pre _ngcontent-ng-c2364348385=""><code _ngcontent-ng-c2364348385="" role="text" data-test-id="code-content" class="code-container no-decoration-radius">pip install matplotlib
pip install numpy
</code></pre>

<br>

#### FdrawSector.py

Esse script desenha um setor hexagonal em um plano complexo usando a biblioteca matplotlib.pyplo
- Para testar o script isolado, descomente as linhas 13, 16, 17 e 18.

<br>

#### FdrawDeploy.py

Esse script desenha uma implantação de células hexagonais para simular uma rede de comunicação celular, juntamente com as posições das estações base (ERBs) no plano complexo.
- Para testar o script isolado, descomente as linhas 13, 16, 19.

<br>

#### Entrega_01.py
    
Este script Python demonstra a criação de um gráfico que representa, por exemplo, uma implantação de rede celular de células hexagonais com 7 ERBs.

<br>

#### Entrega_2.py
    
Este script desenha e simula a distribuição dos pontos de medição em relação às estações base em uma rede de comunicação celular.  É útil para visualizar a distribuição dos pontos de medição em uma rede celular e entender a cobertura do sinal em diferentes áreas em relação às estações base.

<br>

#### Entrega_3.py

Esse Script realiza o  cálculo da potência recebida nos pontos de medição do REM de cada ERB, e também considera a composição das 7 ERBs. Além disso, precisamos considerar que a potência recebida de cada ponto de medição é a maior potência recebida em relação as 7 ERBs. É útil para, por exemplo, entender a distribuição da potência recebida em uma rede celular e como diferentes modelos de propagação afetam essa distribuição.
- Pode ser usado o modelo de propagação de Okumura-Hata ou COST 231

<br>

#### Entrega_04.py

Este script a calcula a taxa de interrupção (outage) de potência  utilizando os modelos de propagação Okumura-Hata e COST 231. Além disso, oferece a funcionalidade de calcular a potência recebida nos pontos de medição do Mapa de Ambiente de Rádio (REM) de cada estação base (ERB). 


### Considerações

Esse projeto usou como referência o projeto <a href="https://github.com/vicentesousa/DCO1020"> Hands-on 01: Uso de modelos de propagação para análises sistêmicas
</a>.<p>
Sinta-se à vontade para contribuir ou sugerir melhorias!