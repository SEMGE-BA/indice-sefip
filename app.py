from flask import Flask, jsonify

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from sefip_parser import SefipParser

app = Flask(__name__)

@app.route("/mes_ini_compt/<int:mes_ini_compt>/mes_fim_compt/<int:mes_fim_compt>/ano_ini_compt/<int:ano_ini_compt>/ano_fim_compt/<int:ano_fim_compt>/dia_ini_pgto/<int:dia_ini_pgto>/mes_ini_pgto/<int:mes_ini_pgto>/ano_ini_pgto/<int:ano_ini_pgto>/dia_fim_pgto/<int:dia_fim_pgto>/mes_fim_pgto/<int:mes_fim_pgto>/ano_fim_pgto/<int:ano_fim_pgto>/tipo_iden_empresa/<tipo_iden_empresa>/cod_fpas/<cod_fpas>/cod_simples/<cod_simples>/opcao/<opcao>/cod_categoria/<cod_categoria>/index_categoria/<index_categoria>/index_opcao/<index_opcao>/index_tipo_iden_empresa/<index_tipo_iden_empresa>/index_cod_fpas/<index_cod_fpas>/index_cod_simples/<index_cod_simples>")
def main(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt, dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto, mes_fim_pgto, ano_fim_pgto, tipo_iden_empresa, cod_fpas, cod_simples, opcao, cod_categoria, index_categoria, index_opcao, index_tipo_iden_empresa, index_cod_fpas, index_cod_simples):
    sefip = SefipParser()
    url = sefip.generate_url(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt, dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto, mes_fim_pgto, ano_fim_pgto, tipo_iden_empresa, cod_fpas, cod_simples, opcao, cod_categoria, index_categoria, index_opcao, index_tipo_iden_empresa, index_cod_fpas, index_cod_simples)
    content = sefip.get_content(url)
    factor = sefip.get_factor(content)

    data = {
        'url': url,
        'fator': factor,
        'competencia': "{}-{}".format(ano_fim_compt, str(mes_fim_compt).zfill(2)),
        'data_pagamento': "{}-{}-{}".format(ano_ini_pgto,str(mes_ini_pgto).zfill(2),str(dia_ini_pgto).zfill(2))
    }

    return jsonify(data)


@app.route("/mes_ini_compt/<int:mes_ini_compt>/mes_fim_compt/<int:mes_fim_compt>/ano_ini_compt/<int:ano_ini_compt>/ano_fim_compt/<int:ano_fim_compt>/dia_ini_pgto/<int:dia_ini_pgto>/mes_ini_pgto/<int:mes_ini_pgto>/ano_ini_pgto/<int:ano_ini_pgto>/dia_fim_pgto/<int:dia_fim_pgto>/mes_fim_pgto/<int:mes_fim_pgto>/ano_fim_pgto/<int:ano_fim_pgto>")

def get_data_to_workers_opts_after_1971229(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt, dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto, mes_fim_pgto, ano_fim_pgto):
    sefip = SefipParser()
    url = sefip.generate_url_for_worker_opts_after_1971229(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt, dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto, mes_fim_pgto, ano_fim_pgto)
    content = sefip.get_content(url)
    factor = sefip.get_factor(content)

    data = {
        'url': url,
        'fator': factor,
        'competencia': "{}-{}".format(ano_fim_compt, str(mes_fim_compt).zfill(2)),
        'data_pagamento': "{}-{}-{}".format(ano_ini_pgto,str(mes_ini_pgto).zfill(2),str(dia_ini_pgto).zfill(2))
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
