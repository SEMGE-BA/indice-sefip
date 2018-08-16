import time
import logging

import pandas as pd
from datetime import datetime
from monthdelta import monthmod

from sefip_parser.tasks import get_factor

logging.basicConfig(level=logging.DEBUG,
                    filename='./log/sefip_parse.log',
                    filemode='a')

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# competencias 01/1967 - 08/2018
# dias para pagamento  01/02/1983 - 06/09/2018

payment_date_start = datetime(1983,2,1,0,0,0)
payment_date_finish = datetime(2018,9,7,0,0,0)
payment_delta = payment_date_finish - payment_date_start

competence_start_date = datetime(1967,1,1,0,0,0)
competence_finish_date = datetime(2018,9,1,0,0,0)
competence_delta = competence_finish_date - competence_start_date

payment_periods = payment_delta.days
competence_periods = monthmod(competence_start_date, competence_finish_date)[0].months

payment_dates_list = pd.date_range(payment_date_start, periods=payment_periods, freq='D')[::-1].tolist()
competences_list = pd.date_range(competence_start_date, periods=competence_periods, freq='M').tolist()

# print(payment_dates_list[0:10], competences_list[0:10], payment_periods, competence_periods)

payments = payment_dates_list
competences = competences_list
limit = 10
delivered_jobs = 0

logging.info('Start the job')

for payment_date in payments:
    if payment_date.isoweekday() != 6 and payment_date.isoweekday() != 7:
        for competence in competences:
            if (delivered_jobs > 0) and (delivered_jobs % limit == 0):
                time.sleep(10)
            str_competence = competence.strftime("%Y-%m-%d")
            str_payment = payment_date.strftime("%Y-%m-%d")
            res = get_factor.delay(str_competence, str_payment)
            delivered_jobs += 1
            result_dict = {
                'task_id': res.id,
                'delivered_jobs': delivered_jobs,
                'data_pagamento': payment_date.strftime("%Y-%m-%d"),
                'competencia': competence.strftime("%Y-%m-%d")
            }
            result_str = str(result_dict)
            logging.info(result_str)
