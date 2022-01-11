import timeit

from ordena_alg.heapsort import heapsort
from ordena_alg.quicksort import quicksort

from tools.cached_data import redis_set

import traceback2 as traceback
from logging42 import logger

async def ordered_array():

    array_scrapping = redis_set()
    
    if(array_scrapping):

        value_quick = array_scrapping.copy()

        logger.info('Iniciando a ordenação dos dados(Heapsort).')
        #print('Iniciando a ordenação dos dados(Heapsort):\n')
        init_ord_heap=timeit.default_timer()    
        heapsort(array_scrapping)
        fim_ord_heap=timeit.default_timer()
        time_heap=fim_ord_heap-init_ord_heap
        logger.info(f'Tempo de execução: {time_heap} segundos.')
        #print(f'\n\nTempo de execução: {time_heap} segundos.\n\n')

        logger.info('Iniciando a ordenação dos dados(Quicksort).')
        #print('Iniciando a ordenação dos dados(Quicksort):\n')
        init_ord_quick=timeit.default_timer()
        quicksort(value_quick, 0, len(value_quick)-1)
        fim_ord_quick=timeit.default_timer()
        time_quick = fim_ord_quick-init_ord_quick
        logger.info(f'Tempo de execução: {time_quick} segundos.')
        #print(f'\n\nTempo de execução: {time_quick} segundos.\n\n')

        if time_quick <= time_heap:
            logger.info(f'tempo de execução do quicksort:{time_quick}.')
            return {'msg': f'tempo de execução do quicksort:{time_quick}.', 'arr':value_quick}
        else:
            logger.info(f'tempo de execução do heapsort:{time_heap}.')
            return {'msg': f'tempo de execução do heapsort:{time_heap}.', 'arr':array_scrapping} 

    else:
        resp  = 'Ocorreu um erro na obtenção dos dados.'
        logger.warning('Ocorreu um erro na obtenção dos dados.')
        #print(f'{resp}\n\n')
    
        return {'msg': resp, 'arr': None}

