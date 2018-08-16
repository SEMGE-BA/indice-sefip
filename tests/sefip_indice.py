CONTENT = """

<html>
    <head>
    <meta NAME="KEYWORDS" CONTENT="Para SUA EMPRESA">
    <link rel="shortcut icon" href="/x.ico">
    <title>Para SUA EMPRESA</title>
    <link rel="stylesheet" type="text/css" href="/Empresa/EditalFgts/Include/link.css">
    <link rel="stylesheet" type="text/css" href="/_css/cef_ns.css">
    <SCRIPT LANGUAGE="javaSCRIPT" SRC="../../Include/FuncoesComuns.js"></SCRIPT>
    <script language="javascript">
    win1=self
    function imprime()
    {
      win1=window.open("/empresa/editalfgts/001/imprimir/imprime.htm",'imprime','toolbar=no,location=no,directories=no,scrollbars=yes,Height=220,Width=400,top=0,left=0,resizable=no')
      if(win1 != self)
        {
            win1.focus();
        }
    }
    </script>
    </head>
    <body onload="imprime()" topmargin="0" leftmargin="0" marginheight="0" marginwidth="0" bgcolor="#e7e7e7" onkeydown="testarPF();" onmousedown="testarPF();">
    <form name="Tabelas">
    <div align=center>
    <table border="0" width="90%" cellspacing="0" cellpadding="0">
        <tr>
            <td valign=middle><img src="../../images/logo.gif"></td><td align=center class="txttituloazulgrande" style="font-size:11pt;font-weight:bolder">Edital Eletrônico</td>
        </tr>
    </table>

    <br>
    <table border="0" width="90%" cellspacing="0" cellpadding="0">
      <tr>
        <td align="left" valign="top">
            <span class="txttituloazulgrande" style="font-size:11pt;font-weight:bolder">:: Coeficientes para Recolhimento Mensal em Atraso</span>
        </td>
      </tr>
    </table>
    <br>
    <table width="90%" BORDER=0 CELLSPACING="0" CELLPADDING=1>
        <tr>
            <td colspan=2 style="text-align:justify"><span class="txtcentral"><b>Por recolhimento mensal ao FGTS em atraso entende-se aquele devido em face do disposto no Art. 15 da Lei n° 8.036/90 e a Contribuição Social instituída pelo Art. 2° da Lei Complementar n° 110/01, quando efetuados após o vencimento regular da competência.</b></span></td>
        </tr>
        <tr><td colspan=2>&nbsp;</td></tr>
        <tr>
            <td colspan=2><span class="txtcentral"><b>Parâmetros Informados:</b></span></td>
        </tr>
        <tr><td colspan=2>&nbsp;</td></tr>
        <tr>
            <td colspan=2><span class="txtcentral"><b>Dados da Competência:</b></span></td>
        </tr>
        <tr>
            <td valign=top width=30%><span class="txtcentral">Mês/Ano:</span></td>
            <td valign=top width=70%><span class="txtcentral">04/1975&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a&nbsp;&nbsp;&nbsp;04/1975</span></td>
        </tr>
        <tr>
            <td valign=top><span class="txtcentral">Data para Pagamento:</span></td>
            <td valign=bottom><span class="txtcentral">10/08/2018&nbsp;&nbsp;&nbsp;a&nbsp;&nbsp;&nbsp;10/08/2018</span></td>
        </tr>
        <tr>
            <td colspan=2>&nbsp;</td>
        </tr>

        <tr>
            <td colspan=2><span class="txtcentral"><b>Dados do Trabalhador:</b></span></td>
        </tr>
        <tr>
            <td valign=top><span class="txtcentral">Opção:</span></td>
            <td valign=top><span class="txtcentral" id="hddTxtOpcao">Optantes após 22/09/1971</span></td>
        </tr>
        <tr>
            <td valign=top><span class="txtcentral">Categoria:</span></td>
            <td valign=bottom><span class="txtcentral" id="hddTxtCategoria">
            1 - Trabalhador
            </span></td>
        </tr>

        <!--++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-->


    </div>
        <!--++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            valida as datas e competencias apuradas
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-->
        <!--++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            apura o periodo de competencias e de datas
        --++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-->
        <!--include virtual ="/Empresa/EditalFgts/Include/ValidarDatasComptEdital.asp"-->
        <!--'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
             popula as informações comuns de verificação da CS
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-->

        <!--++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            obtenção do edital para cada data de pagamento informada
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-->


        <tr>
            <td colspan=2>&nbsp;</td>
        </tr>
        <tr>
            <td colspan=2><span class="txtcentral"><b>Alíquotas:</b></span></td>
        </tr>
        <tr>
            <td valign=middle><span class="txtcentral">FGTS:</span></td>
            <td valign=bottom><span class="txtcentral" id="perc">8%</span></td>
        </tr>
        <tr>
            <td valign=middle><span class="txtcentral">Contribuição Social:</span></td>
            <td valign=bottom><span class="txtcentral" id="percs">Parâmetros indicam não incidência dessa Contribuição</span></td>
        </tr>
        <tr><td colspan=2>&nbsp;</td></tr>
        <tr>
            <td colspan=2 style="TEXT-ALIGN:justify"><span class="txtcentral" style="font-weight:bolder" id="txtFim">
            A tabela apresentada a seguir está em conformidade com os parâmetros informados acima.
            </span>
            </td>
        </tr>
        <!---->
        <tr height=30>
        <td colspan=2 align=right><IMG src="/empresa/editalfgts/Images/botimprimir.gif"
        onclick="Imprimir()" style="cursor:hand; border:0"></td>
        </tr>


    <div align=center>
    <table border=0 width="90%" cellpadding="0" cellspacing=1>
        <tr>
          <td width="15%" rowspan="2" align=center valign="middle" class=cellaranjac>Data de<br>Pagamento</td>
          <td width="75%" colspan="5" align=center valign="middle" class=cellaranjac>Competências</td>
        </tr>
        <tr>
          <td width="15%" class=cellaranjac nowrap>
          De 03 / 1975<br>A&nbsp;&nbsp;&nbsp;05 / 1975
          </td>
          <td width="15%" class=cellaranjac nowrap>
          &nbsp;
          </td>
          <td width="15%" class=cellaranjac nowrap>
          &nbsp;
          </td>
          <td width="15%" class=cellaranjac nowrap>
          &nbsp;
          </td>
          <td width="15%" class=cellaranjac nowrap>
          &nbsp;
          </td>
        </tr>

                                  <tr height=16 >
                                    <td align="center"><span class=txtcentral>10/08/2018</span></td>

                                      <td  align="right"><span class=txtcentral>0,067794218</span></td>

                                      <td  align="right"><span class=txtcentral>&nbsp;</span></td>

                                      <td  align="right"><span class=txtcentral>&nbsp;</span></td>

                                      <td  align="right"><span class=txtcentral>&nbsp;</span></td>

                                      <td  align="right"><span class=txtcentral>&nbsp;</span></td>

                                  </tr>
                    <tr bgcolor="#F07020"><td colspan="8"><img src="../../images/transparente.gif" width="1" height="1"></td></tr>

                </table>

    <!---->
    <table border=0 width=90% cellspacing=0 cellpadding=0>
    <tr height=30>
        <td colspan=2 align=right><IMG src="/empresa/editalfgts/Images/botimprimir.gif"
        onclick="Imprimir()" style="cursor:hand; border:0"></td>
        </tr>
    </table></div>
    <br><br>
    </form>
    </body>
    <br>
    <br>
    </html>
"""
