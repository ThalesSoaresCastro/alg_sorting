import requests
import time
url_api = 'http://challenge.dienekes.com.br/api/numbers'

import traceback2 as traceback
from logging42 import logger

def scrapping_data():
    data=[]
    num=1
    num_attempt=1
    try:
        while(num != -1 and num_attempt <= 5):

            if int(time.time()%5) == 0:
                logger.info('Processo ainda sendo executado, aguarde...')
                #print('Processo ainda sendo executado, aguarde...')

            time.sleep(0.5**num_attempt)
            response = requests.get(f'{url_api}?page={num}', timeout=5)
            #print('1 while - len:', len(response.json()['numbers']))

            if response.status_code != 200:
                num_attempt+=1
                logger.info(f'Erro na requisição da página {num}, tentativa anti-falha número {num_attempt}...')
                #print(f'Erro na requisição da página {num}, tentativa anti-falha número {num_attempt}...')
            else:
                num_attempt=1
                if response.json()['numbers']:
            #if response.status_code == 200 and response.json()['numbers']:
                #print(response.json())
                    data += response.json()['numbers']
                    num += 1
            #if not response.json()['numbers']:
                else:
                    num=-1
                    return data    

            
    except Exception as e:
        #print(f'Error: Não foi possível obter os dados\n\n {e}')
        logger.error(traceback.format_exc())
        return None
    finally:
        logger.info('Data error: ', len(data))
        #print('Data error: ', len(data))

    logger.info(f'amount of data: {len(data)}')
    return data