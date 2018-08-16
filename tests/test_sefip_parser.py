from os import path

from sefip_parser import SefipParser

from tests.sefip_indice import CONTENT

def test_generate_url():
    sefip = SefipParser()
    url = sefip.generate_url_for_worker_opts_after_1971229(4,4,1975,1975,2018,8,10,2018,8,10)

    expected_url = 'https://webp.caixa.gov.br/Empresa/EditalFGTS/003/001/Fgepw001a.asp?MesICompt=04&MesFCompt=04&AnoICompt=1975&AnoFCompt=1975&DiaIPgto=10&MesIPgto=08&AnoIPgto=2018&DiaFPgto=10&MesFPgto=08&AnoFPgto=2018&TipIdenEmp=&CodFpas=&CodSimples=&Opcao=19710923&CodCategoria=1&ICategoria=1&IOpcao=6&ITipIdenEmp=0&ICodFpas=0&ICodSimples=0'
    assert expected_url == url

def test_get_factor():
    sefip = SefipParser()
    factor = sefip.get_factor(CONTENT)
    assert 0.067794218 == factor
