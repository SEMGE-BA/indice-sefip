# indice-sefip

#### Fonte dos dados

* Tabela de Coeficientes para Recolhimento em Atraso - https://webp.caixa.gov.br/empresa/EditalFGTS/005/004/fgepw004.asp
* https://webp.caixa.gov.br/empresa/EditalFGTS/003/001/fgepw001.asp

Parametros utilizados:

* Opção FGTS:	Optantes após 22/09/1971
* Categoria: Trabalhador

#### Exemplos

`curl http://localhost:5000/mes_ini_compt/04/mes_fim_compt/04/ano_ini_compt/1975/ano_fim_compt/1975/dia_ini_pgto/10/mes_ini_pgto/08/ano_ini_pgto/2018/dia_fim_pgto/10/mes_fim_pgto/08/ano_fim_pgto/2018/tipo_iden_empresa/1/cod_fpas/000/cod_simples/1/opcao/19710923/cod_categoria/1/index_categoria/1/index_opcao/6/index_tipo_iden_empresa/0/index_cod_fpas/0/index_cod_simples/0`

irá gerar essa url

`https://webp.caixa.gov.br/Empresa/EditalFGTS/003/001/Fgepw001a.asp?MesICompt=04&MesFCompt=04&AnoICompt=1975&AnoFCompt=1975&DiaIPgto=10&MesIPgto=08&AnoIPgto=2018&DiaFPgto=10&MesFPgto=08&AnoFPgto=2018&TipIdenEmp=&CodFpas=&CodSimples=&Opcao=19710923&CodCategoria=1&ICategoria=1&IOpcao=6&ITipIdenEmp=0&ICodFpas=0&ICodSimples=0`

json de retorno:

```json
{
  "competencia": "1975-04",
  "data_pagamento": "2018-08-10",
  "fator": 0.067794218,
  "text": "Para SUA EMPRESAwin1=selffunction imprime(){  win1=window.open(\"/empresa/editalfgts/001/imprimir/imprime.htm\",'imprime','toolbar=no,location=no,directories=no,scrollbars=yes,Height=220,Width=400,top=0,left=0,resizable=no')  if(win1 != self) \t{\t\twin1.focus();\t}}  Edital Eletrnico    :: Coeficientes para Recolhimento Mensal em Atraso     Por recolhimento mensal ao FGTS em atraso entende-se aquele devido em face do disposto no Art. 15 da Lei n 8.036/90 e a Contribuio Social instituda pelo Art. 2 da Lei Complementar n 110/01, quando efetuados aps o vencimento regular da competncia.  \u00a0  Parmetros Informados:  \u00a0  Dados da Competncia:   Ms/Ano: 04/1975\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0\u00a0a\u00a0\u00a0\u00a004/1975   Data para Pagamento: 10/08/2018\u00a0\u00a0\u00a0a\u00a0\u00a0\u00a010/08/2018   \u00a0   Dados do Trabalhador:   Opo: Optantes aps 22/09/1971   Categoria: \t\t1 - Trabalhador\t\t          \u00a0   Alquotas:   FGTS: 8%   Contribuio Social: Parmetros indicam no incidncia dessa Contribuio  \u00a0  \t\tA tabela apresentada a seguir est em conformidade com os parmetros informados acima.\t\t        Data dePagamento Competncias   \t  De 03 / 1975A\u00a0\u00a0\u00a005 / 1975\t   \t  \u00a0\t   \t  \u00a0\t   \t  \u00a0\t   \t  \u00a0\t     10/08/2018 0,067794218 \u00a0 \u00a0 \u00a0 \u00a0      ",
  "url": "https://webp.caixa.gov.br/Empresa/EditalFGTS/003/001/Fgepw001a.asp?MesICompt=04&MesFCompt=04&AnoICompt=1975&AnoFCompt=1975&DiaIPgto=10&MesIPgto=08&AnoIPgto=2018&DiaFPgto=10&MesFPgto=08&AnoFPgto=2018&TipIdenEmp=&CodFpas=&CodSimples=&Opcao=19710923&CodCategoria=1&ICategoria=1&IOpcao=6&ITipIdenEmp=0&ICodFpas=0&ICodSimples=0"
}
```
