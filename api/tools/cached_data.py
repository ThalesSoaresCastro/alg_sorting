import timeit
import os
import redis
import json


import traceback2 as traceback
from logging42 import logger

from dotenv import load_dotenv
load_dotenv()

from services.scrapping import scrapping_data

PORT_REDIS=os.getenv('REDIS_PORT')
HOST_REDIS=os.getenv('REDIS_HOST_NAME')
REDIS_PASSWORD=os.getenv('REDIS_PASSWORD')

cache = redis.Redis(#host='localhost',
                    host=HOST_REDIS,
                    #port=6556,
                    port=PORT_REDIS,
                    #password='redis')
                    password=REDIS_PASSWORD)

def scrapping():
    #print('Iniciando o scrapping dos dados:\n')
    logger.info('Iniciando processo de extração dos dados da api')
    init_scpt=timeit.default_timer()    
    arr_scrapping = scrapping_data()
    fim_scpt=timeit.default_timer() 
    if arr_scrapping:
        logger.info(f'\nQuantidade de elementos obtidos: {len(arr_scrapping)}.\
            \nTempo de execução: {fim_scpt-init_scpt} segundos.\n\n')
        #print(f'\nQuantidade de elementos obtidos: {len(arr_scrapping)}.\
        #    \nTempo de execução: {fim_scpt-init_scpt} segundos.\n\n')
        return arr_scrapping
    else:
        logger.warning('Erro na obtenção dos dados da api.')
        #print('Error na obtenção dos dados da api.')    
        return None

def redis_set():
    if not cache.get(name='array'):
        logger.info('Dados não estão na cache')
        #print('\n\nNão está na cache\n\n')
        list_array = []
        array_data = scrapping()
    
        if array_data:
            cache.set(name='array', value=json.dumps(array_data))
            list_array = json.loads(cache.get('array'))
            return list_array
        else:
            return None
    else:
        #print('\n\nEstá na cache\n\n')
        logger.info('Dados se encontram na cache')
        return json.loads(cache.get('array'))
