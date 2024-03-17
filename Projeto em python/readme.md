
# Hands-on 01: Uso de modelos de propagação para análises sistêmicas

## Parte 01: Avaliação de cobertura celular


## Visão Geral
Este programa implementa um modelo de propagação de onda para calcular a taxa de outage e a potência recebida em pontos de medição. O modelo considera um cenário com 7 células hexagonais e utiliza o modelo de Okumura-Hata ou COST 231 para calcular o Path Loss.
## Objetivos

- Criar um Grid Hexagonal para modelar cobertura de Estações Rádio Base;
- Analisar potência recebida visualmente por meio de Radio Environment Maps (REMs);
- Fazer exemplo de estudo de Outage de potência.


## Uso
<strong> OBS: caso queira entender a construção de cada código, leia o <a href=“https://github.com/FllavioAndrade/DCO1020/tree/main/Projeto%20em%20python/Script“> readme.md </a> da pasta script</strong>

1. Execute o arquivo que se encontra em:
   - dist/Comunicações Móveis/Comunicações Móveis.exe (será aberto o terminal) 
2. Selecione o modo de operação desejado:
   - Opção 1: Calcular a taxa de interrupção de potência.
   - Opção 2: Calcular a potência recebida nos pontos de medição para cada Mapa de Ambiente de Rádio (REM) da estação base.
3. Escolha o modelo de propagação:
   - Okumura-Hata: Adequado para ambientes urbanos.
   - COST 231: Outro modelo de propagação para ambientes urbanos, porém mais confiável para frequeências acima de 900MHz.
4. Insira o raio da célula hexagonal (em metros).
5. Para a Opção 2 (calcular a potência recebida nos pontos de medição):
   - Selecione a frequência da portadora:
     - 1: 800MHz
     - 2: 900MHz
     - 3: 1800MHz
     - 4: 1900MHz
     - 5: 2100MHz
6. Se desejar, continue executando o script ou saia.
     
### Considerações

Esse projeto usou como referência o projeto <a href="https://github.com/vicentesousa/DCO1020"> Hands-on 01: Uso de modelos de propagação para análises sistêmicas
</a>.<p>
Sinta-se à vontade para contribuir ou sugerir melhorias!
