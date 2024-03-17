function vtPr = calculateReceivePower(Ga, Xs, ptx, Lp)
% PURPOSE: Cálculo da potência recebida (pode ser um vetor) em Watts
%
% USAGE: vtPr = calculateReceivePower(Ga, Xs, ptx, Lp)
%
% INPUTS:
% - Ga: ganho da antena (pode ser um vetor) em dBi
% - Xs: amostra de shadowing (pode ser um vetor) em dB
% - ptx: potência de transmissão (pode ser um vetor) em W
% - Lp: Perda de Percurso (pode ser um vetor) em escala linear
%
% OUTPUTS:
%  - vtPr: vetor coluna com as potências recebidas em Watts
%
% EXAMPLE: vtPr1 = calculateReceivePower(16, [-1.1853 ; -0.7236 ], 0.1250, [5.2727;1.0278]*1e8)
%
% SEE ALSO: fUL_sim_Skelenton
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% AUTHOR(S): Vicente 
% LAST UPDATE: 2015-05-31 at 16:00h
% REFERENCES:
% COPYRIGHT 2015 by UFRN
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
