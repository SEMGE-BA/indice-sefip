from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import subprocess

app = Flask(__name__)

def process_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_content(url):
    result = subprocess.run(['curl', url, '--insecure'], stdout=subprocess.PIPE)
    content = result.stdout
    content = str(content, 'utf-8', errors='ignore')
    content = content.replace('\r\n', '')
    return content

def generate_url(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt, dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto, mes_fim_pgto, ano_fim_pgto, tipo_iden_empresa, cod_fpas, cod_simples, opcao, cod_categoria, index_categoria, index_opcao, index_tipo_iden_empresa, index_cod_fpas, index_cod_simples):

    url = 'https://webp.caixa.gov.br/Empresa/EditalFGTS/004/001/Fgepw001a.asp?'
    url += 'MesICompt=' + str(mes_ini_compt).zfill(2) + '&MesFCompt=' + str(mes_fim_compt).zfill(2)
    url += '&AnoICompt=' + str(ano_ini_compt) + '&AnoFCompt=' + str(ano_fim_compt)
    url += '&DiaIPgto=' + str(dia_ini_pgto).zfill(2) + '&MesIPgto=' + str(mes_ini_pgto).zfill(2) + '&AnoIPgto=' + str(ano_ini_pgto)
    url += '&DiaFPgto=' + str(dia_fim_pgto).zfill(2) + '&MesFPgto=' + str(mes_fim_pgto).zfill(2) + '&AnoFPgto=' + str(ano_fim_pgto)
    url += '&TipIdenEmp=' + str(tipo_iden_empresa) + '&CodFpas=' + str(cod_fpas) + '&CodSimples=' + str(cod_simples)
    url += '&Opcao=' + str(opcao) + '&CodCategoria=' + str(cod_categoria) + '&ICategoria=' + str(index_categoria)
    url += '&IOpcao=' + str(index_opcao) + '&ITipIdenEmp=' + str(index_tipo_iden_empresa) + '&ICodFpas=' + str(index_cod_fpas) + '&ICodSimples=' + str(index_cod_simples)

    return url

@app.route("/mes_ini_compt/<int:mes_ini_compt>/mes_fim_compt/<int:mes_fim_compt>/ano_ini_compt/<int:ano_ini_compt>/ano_fim_compt/<int:ano_fim_compt>/dia_ini_pgto/<int:dia_ini_pgto>/mes_ini_pgto/<int:mes_ini_pgto>/ano_ini_pgto/<int:ano_ini_pgto>/dia_fim_pgto/<int:dia_fim_pgto>/mes_fim_pgto/<int:mes_fim_pgto>/ano_fim_pgto/<int:ano_fim_pgto>/tipo_iden_empresa/<tipo_iden_empresa>/cod_fpas/<cod_fpas>/cod_simples/<cod_simples>/opcao/<opcao>/cod_categoria/<cod_categoria>/index_categoria/<index_categoria>/index_opcao/<index_opcao>/index_tipo_iden_empresa/<index_tipo_iden_empresa>/index_cod_fpas/<index_cod_fpas>/index_cod_simples/<index_cod_simples>")
def main(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt, dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto, mes_fim_pgto, ano_fim_pgto, tipo_iden_empresa, cod_fpas, cod_simples, opcao, cod_categoria, index_categoria, index_opcao, index_tipo_iden_empresa, index_cod_fpas, index_cod_simples):
    url = generate_url(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt, dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto, mes_fim_pgto, ano_fim_pgto, tipo_iden_empresa, cod_fpas, cod_simples, opcao, cod_categoria, index_categoria, index_opcao, index_tipo_iden_empresa, index_cod_fpas, index_cod_simples)

    r = get_content(url)
    soup = process_content(r)
    spans = soup.find_all('span', {'class': 'txtcentral8'})
    factor = 0

    for i, span in enumerate(spans):
        content_tag = span.get_text().strip().replace('.','').replace(',','.')
        try:
            factor = float(content_tag)
        except:
            print("{} is not number".format(content_tag))

    data = {
        'url': url,
        'text': soup.get_text(),
        'fator': factor,
        'mes_competencia': "{}-{}".format(ano_fim_compt, str(mes_fim_compt).zfill(2)),
        'data_pagamento': "{}-{}-{}".format(ano_ini_pgto,str(mes_ini_pgto).zfill(2),str(dia_ini_pgto).zfill(2))
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)


   # Exemplo de url: http://0.0.0.0:5000/mes_ini_compt/04/mes_fim_compt/06/ano_ini_compt/2007/ano_fim_compt/2007/dia_ini_pgto/30/mes_ini_pgto/05/ano_ini_pgto/2017/dia_fim_pgto/30/mes_fim_pgto/05/ano_fim_pgto/2017/tipo_iden_empresa/1/cod_fpas/000/cod_simples/1/opcao/1967/cod_categoria/1/index_categoria/1/index_opcao/1/index_tipo_iden_empresa/1/index_cod_fpas/3/index_cod_simples/1
