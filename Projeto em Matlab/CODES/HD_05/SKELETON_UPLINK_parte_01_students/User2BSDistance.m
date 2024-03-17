function vtUser2BSDistance = User2BSDistance( mtSectorPos, vtBs, iERBTarget )
% PURPOSE: Calcular a distância entre os usuários da ERB target
% identificada por "iERBTarget" e a ERB Central 
%
% USAGE: vtUser2BSDistance = User2BSDistance( mtSectorPos, vtBs, ibInter)
%
% INPUTS:
% - mtSectorPos: matriz com a posição (complexa) de cada usuário em relação
%                as 7 ERBS (linhas: usuários; e nas colunas: ERB)
% - vtBs: vetor com a posição de cada ERBs (a primeira posição é da ERB
%         Central e as demais são interferentes) 
% - iERBTarget: índice da ERB alvo para o cálculo da distância
%
% OUTPUTS:
%  - vtUser2BSDistance: vetor coluna com as distâncias dos usuários da ERB
%                        identificada por "iERBTarget" e a ERB Central
%                        (distância na mesma unidade que mtSectorPos e vtBs) 
%
% EXAMPLE: para um grid com 2 ERBs:
%          vtUser2BSDistance = User2BSDistance(1e2*[0.11+0.34i 1.13+0.39i; -0.15+0.085i 0.52+0.27i], [0 75+43.3i], 1 ) 
%          vtUser2BSDistance = User2BSDistance(1e2*[0.11+0.34i 1.13+0.39i; -0.15+0.085i 0.52+0.27i], [0 75+43.3i], 2 ) 
%
% SEE ALSO: fUL_sim_Skelenton
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUTHOR(S): Vicente 
% LAST UPDATE: 2015-05-31 at 16:00h
% REFERENCES:
% COPYRIGHT 2015 by UFRN
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
