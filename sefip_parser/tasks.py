from __future__ import absolute_import, unicode_literals
import os
import json
import csv

from .celery import app
from . import SefipParser

def save_to_json(data, filename):
    a = []
    if not os.path.isfile(filename):
        with open(filename, mode='w') as f:
            f.write(json.dumps(a))

    json_data = json.loads(open(filename).read())

    json_data.append(data)

    with open(filename, mode='w') as f:
        json.dump(json_data, f)

def save_to_csv(data, filename):
    fields = [data['data_pagamento'], data['competencia'], data['fator'], data['url']]
    with open(filename, mode='a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

@app.task
def get_factor(competence, date_payment):
    competence_year, competence_month, competence_day = competence.split('-')
    payment_year, payment_month, payment_day = date_payment.split('-')
    sefip = SefipParser()
    url = sefip.generate_url_for_worker_opts_after_1971229(competence_month, competence_month, competence_year, competence_year, payment_year, payment_month, payment_day, payment_year, payment_month, payment_day)
    content = sefip.get_content(url)
    factor = sefip.get_factor(content)

    data = {
        'url': url,
        'fator': factor,
        'competencia': competence,
        'data_pagamento': date_payment
    }

    jsonfile = './dataset/fatores_sefip.json'
    csvfile = './dataset/fatores_sefip.csv'
    save_to_json(data, jsonfile)
    save_to_csv(data, csvfile)

    return data
