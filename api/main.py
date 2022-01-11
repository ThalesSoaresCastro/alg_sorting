import timeit

from services.scrapping import scrapping_data
from ordena_alg.heapsort import heapsort
from ordena_alg.quicksort import quicksort


import random
def rand_arr(tam):
    arr=[]
    for i in range(tam):
        arr.append(random.randrange(0,1000))
    
    return arr

def main():
    """
        Fazendo scrapping dos dados...
    """
    print('Iniciando o scrapping dos dados:\n')
    init_scpt=timeit.default_timer()    
    value_scrapping = scrapping_data()
    fim_scpt=timeit.default_timer()
    
    """
        Fazendo a ordenação dos dados...
    """
    if(value_scrapping):
        print(f'\nQuantidade de elementos obtidos: {len(value_scrapping)}.\
            \nTempo de execução: {fim_scpt-init_scpt} segundos.\n\n')

        value_quick = value_scrapping.copy()

        print('Iniciando a ordenação dos dados(Heapsort):\n')
        init_ord_heap=timeit.default_timer()    
        heapsort(value_scrapping)
        fim_ord_heap=timeit.default_timer()
        time_heap=fim_ord_heap-init_ord_heap
        print(f'\n\nTempo de execução: {time_heap} segundos.\n\n')

        print('Iniciando a ordenação dos dados(Quicksort):\n')
        init_ord_quick=timeit.default_timer()
        quicksort(value_quick, 0, len(value_quick)-1)
        fim_ord_quick=timeit.default_timer()
        time_quick = fim_ord_quick-init_ord_quick
        print(f'\n\nTempo de execução: {time_quick} segundos.\n\n')

        if time_quick <= time_heap:
            return value_quick
        else:
            return value_scrapping

    else:
        print('Ocorreu um erro na obtenção dos dados.\n\n')
    
        return None

    #a = [4,3,2,1,8,7,6,5,5,5,5,7,1,24,8,9,543]
    #a = rand_arr(1000)
    #print(f'\nINICIAL - A: {a}\n')
    #heapsort(a)
    
    #quicksort(a, 0, (len(a)-1))
    #print('A: ', a)

#if __name__ == '__main__':
#    main()


async def ordered_array():
    """
        Fazendo scrapping dos dados...
    """
    print('Iniciando o scrapping dos dados:\n')
    init_scpt=timeit.default_timer()    
    value_scrapping = scrapping_data()
    fim_scpt=timeit.default_timer()
    
    """
        Fazendo a ordenação dos dados...
    """
    if(value_scrapping):
        print(f'\nQuantidade de elementos obtidos: {len(value_scrapping)}.\
            \nTempo de execução: {fim_scpt-init_scpt} segundos.\n\n')

        value_quick = value_scrapping.copy()

        print('Iniciando a ordenação dos dados(Heapsort):\n')
        init_ord_heap=timeit.default_timer()    
        heapsort(value_scrapping)
        fim_ord_heap=timeit.default_timer()
        time_heap=fim_ord_heap-init_ord_heap
        print(f'\n\nTempo de execução: {time_heap} segundos.\n\n')

        print('Iniciando a ordenação dos dados(Quicksort):\n')
        init_ord_quick=timeit.default_timer()
        quicksort(value_quick, 0, len(value_quick)-1)
        fim_ord_quick=timeit.default_timer()
        time_quick = fim_ord_quick-init_ord_quick
        print(f'\n\nTempo de execução: {time_quick} segundos.\n\n')

        if time_quick <= time_heap:
            return {'msg': f'tempo de execução do quicksort:{time_quick}.', 'arr':value_quick}
        else:
            return {'msg': f'tempo de execução do heapsort:{time_heap}.', 'arr':value_scrapping} 

    else:
        resp  = 'Ocorreu um erro na obtenção dos dados.'
        print(f'{resp}\n\n')
    
        return {'msg': resp, 'arr': None}

