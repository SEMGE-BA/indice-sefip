import subprocess

from bs4 import BeautifulSoup


class SefipParser(object):
    ROOT_URL = 'https://webp.caixa.gov.br'
    BASE_PATH = '/Empresa/EditalFGTS/003/001/Fgepw001a.asp'

    def base_url(self):
        return "{}{}".format(self.ROOT_URL, self.BASE_PATH)

    def process_content(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def generate_url(self, mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt,
                    dia_ini_pgto, mes_ini_pgto, ano_ini_pgto, dia_fim_pgto,
                    mes_fim_pgto, ano_fim_pgto, tipo_iden_empresa, cod_fpas,
                    cod_simples, opcao, cod_categoria, index_categoria,
                    index_opcao, index_tipo_iden_empresa, index_cod_fpas, index_cod_simples):

        url = self.base_url() + '?'
        url += 'MesICompt=' + str(mes_ini_compt).zfill(2) + '&MesFCompt=' + str(mes_fim_compt).zfill(2)
        url += '&AnoICompt=' + str(ano_ini_compt) + '&AnoFCompt=' + str(ano_fim_compt)
        url += '&DiaIPgto=' + str(dia_ini_pgto).zfill(2) + '&MesIPgto=' + str(mes_ini_pgto).zfill(2) + '&AnoIPgto=' + str(ano_ini_pgto)
        url += '&DiaFPgto=' + str(dia_fim_pgto).zfill(2) + '&MesFPgto=' + str(mes_fim_pgto).zfill(2) + '&AnoFPgto=' + str(ano_fim_pgto)
        url += '&TipIdenEmp=' + str(tipo_iden_empresa) + '&CodFpas=' + str(cod_fpas) + '&CodSimples=' + str(cod_simples)
        url += '&Opcao=' + str(opcao) + '&CodCategoria=' + str(cod_categoria) + '&ICategoria=' + str(index_categoria)
        url += '&IOpcao=' + str(index_opcao) + '&ITipIdenEmp=' + str(index_tipo_iden_empresa) + '&ICodFpas=' + str(index_cod_fpas) + '&ICodSimples=' + str(index_cod_simples)

        return url

    def generate_url_for_worker_opts_after_1971229(self, mes_fim_compt, mes_ini_compt, ano_ini_compt, ano_fim_compt,
                                                        ano_ini_pgto, mes_ini_pgto, dia_ini_pgto,
                                                        ano_fim_pgto, mes_fim_pgto, dia_fim_pgto):

        tipo_iden_empresa = ''
        cod_fpas = ''
        cod_simples = ''
        opcao = 19710923
        cod_categoria = 1
        index_categoria = 1
        index_opcao = 6
        index_tipo_iden_empresa = 0
        index_cod_fpas = 0
        index_cod_simples = 0

        url = self.generate_url(mes_ini_compt, mes_fim_compt, ano_ini_compt, ano_fim_compt,
                                dia_ini_pgto, mes_ini_pgto, ano_ini_pgto,
                                dia_fim_pgto, mes_fim_pgto, ano_fim_pgto,
                                tipo_iden_empresa, cod_fpas, cod_simples, opcao,
                                cod_categoria, index_categoria, index_opcao, index_tipo_iden_empresa,
                                index_cod_fpas, index_cod_simples)

        return url

    def get_content(self, url):
        result = subprocess.run(['curl', url, '--insecure'], stdout=subprocess.PIPE)
        content = result.stdout
        content = str(content, 'utf-8', errors='ignore')
        content = content.replace('\r\n', '')
        return content

    def get_factor(self, content):
        soup = self.process_content(content)
        spans = soup.find_all('span', {'class': 'txtcentral'})
        factor = 0.0

        for i, span in enumerate(spans):
            content_tag = span.get_text().strip().replace('.','').replace(',','.')
            if content_tag != '':
                try:
                    factor = float(content_tag)
                except:
                    pass

        return factor
