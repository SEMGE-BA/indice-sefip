from flask import Flask
from flask import request

app = Flask(__name__)

def generate_url(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt, dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto, mes_fim_pgto, ano_fim_pgto, tipo_iden_empresa, cod_fpas, cod_simples, opcao, cod_categoria, index_categoria, index_opcao, index_tipo_iden_empresa, index_cod_fpas, index_cod_simples):
    
    url = 'https://webp.caixa.gov.br/Empresa/EditalFGTS/004/001/Fgepw001a.asp'
    url += '&MesICompt=' + str(mes_ini_compt) + '&MesFCompt=' + str(mes_fim_compt)
    url += '&AnoICompt=' + str(ano_ini_compt) + '&AnoFCompt=' + str(ano_fim_compt)	
    url += '&DiaIPgto=' + str(dia_ini_pgto) + '&MesIPgto=' + str(mes_ini_pgto) + '&AnoIPgto=' + str(ano_ini_pgto)
    url += '&DiaFPgto=' + str(dia_fim_pgto) + '&MesFPgto=' + str(mes_fim_pgto) + '&AnoFPgto=' + str(ano_fim_pgto) 
    url += '&TipIdenEmp=' + str(tipo_iden_empresa) + '&CodFpas=' + str(cod_fpas) + '&CodSimples=' + str(cod_simples)
    url += '&Opcao=' + str(opcao) + '&CodCategoria=' + str(cod_categoria) + '&ICategoria=' + str(index_categoria)
    url += '&IOpcao=' + str(index_opcao) + '&ITipIdenEmp=' + str(index_tipo_iden_empresa) + '&ICodFpas=' + str(index_cod_fpas) + '&ICodSimples=' + str(index_cod_simples)

    return url

@app.route("/mes_ini_compt/<int:mes_ini_compt>/mes_fim_compt/<int:mes_fim_compt>/ano_ini_compt/<int:ano_ini_compt>/ano_fim_compt/<int:ano_fim_compt>/dia_ini_pgto/<int:dia_ini_pgto>/mes_ini_pgto/<int:mes_ini_pgto>/ano_ini_pgto/<int:ano_ini_pgto>/dia_fim_pgto/<int:dia_fim_pgto>/mes_fim_pgto/<int:mes_fim_pgto>/ano_fim_pgto/<int:ano_fim_pgto>/tipo_iden_empresa/<tipo_iden_empresa>/cod_fpas/<cod_fpas>/cod_simples/<cod_simples>/opcao/<opcao>/cod_categoria/<cod_categoria>/index_categoria/<index_categoria>/index_opcao/<index_opcao>/index_tipo_iden_empresa/<index_tipo_iden_empresa>/index_cod_fpas/<index_cod_fpas>/index_cod_simples/<index_cod_simples>")
def main(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt, dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto, mes_fim_pgto, ano_fim_pgto, tipo_iden_empresa, cod_fpas, cod_simples, opcao, cod_categoria, index_categoria, index_opcao, index_tipo_iden_empresa, index_cod_fpas, index_cod_simples):
    url = generate_url(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt, dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto, mes_fim_pgto, ano_fim_pgto, tipo_iden_empresa, cod_fpas, cod_simples, opcao, cod_categoria, index_categoria, index_opcao, index_tipo_iden_empresa, index_cod_fpas, index_cod_simples)
    return url

if __name__ == "__main__":
    app.run()


   # Exemplo de url: http://0.0.0.0:5000/mes_ini_compt/04/mes_fim_compt/06/ano_ini_compt/2007/ano_fim_compt/2007/dia_ini_pgto/30/mes_ini_pgto/05/ano_ini_pgto/2017/dia_fim_pgto/30/mes_fim_pgto/05/ano_fim_pgto/2017/tipo_iden_empresa/1/cod_fpas/000/cod_simples/1/opcao/1967/cod_categoria/1/index_categoria/1/index_opcao/1/index_tipo_iden_empresa/1/index_cod_fpas/3/index_cod_simples/1